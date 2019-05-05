#!/usr/bin/env python3

#in case you want to delete the kl stores
#redis-cli --scan --pattern k1:* | xargs redis-cli unlink
#redis-cli --scan --pattern k2:* | xargs redis-cli unlink

import redis

# define our connection information for Redis
# Replaces with your configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""

def join_list_elements(list):
    result = ""
    for i in list:
        result = result + str(i)
    return result

def aggr_klstore (name1, aggr, func):

    # create the Redis Connection object
    try:

        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

        # get the keys in name1 klstore
        keys = r.keys(name1 + ':*')

        # get each key of keys
        for key in keys:
            list = r.lrange(key,0,-1)
            #transform string values into integers
            numbers = [int(v) for v in list]
            i = -1
            for value in r.lrange(key,0,-1):
                i = i + 1
                # delete the value of key
                r.lrem(key,i,value)

            #if aggr is not an empty object execute the aggregation
            if aggr:
                # add the value of aggregation in klstore
                if aggr == 'max':
                    r.lpush(key,max(numbers))
                elif aggr == 'count':
                    r.lpush(key,len(numbers))
                elif aggr == 'min':
                    r.lpush(key,min(numbers))
                elif aggr == 'sum':
                    r.lpush(key,sum(numbers))
                elif aggr == 'avg':
                    r.lpush(key, sum(numbers)/float(len(numbers)))

            #if aggr is an empty object execute the func
            else:
                r.lpush(key,func(numbers))


    except Exception as e:
        print(e)

if __name__ == '__main__':
    aggr_klstore ('k1', 'max', join_list_elements)
    # aggr_klstore ('k1', 'count', join_list_elements)
    # aggr_klstore ('k1', 'min', join_list_elements)
    # aggr_klstore ('k1', 'sum', join_list_elements)
    # aggr_klstore ('k1', 'avg', join_list_elements)
    # aggr_klstore ('k1',  '', join_list_elements)
    # aggr_klstore ('k2', 'max', join_list_elements)
    # aggr_klstore ('k2', 'count', join_list_elements)
    # aggr_klstore ('k2', 'min', join_list_elements)
    # aggr_klstore ('k2', 'sum', join_list_elements)
    # aggr_klstore ('k2', 'avg', join_list_elements)
    aggr_klstore ('k2',  '', join_list_elements)
