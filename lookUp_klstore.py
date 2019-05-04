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

def lookUp_klstore (name1, name2):

    # create the Redis Connection object
    try:

        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

        # get the keys from name1 and name2 klstores
        keys_name1 = r.keys(name1 + ':*')

        # get each key of keys
        for key in keys_name1:
            # i is for index in list
            i = -1
            # get every value of key
            for value in r.lrange(key,0,-1)
                i = i + 1
                # delete the value of key
                r.lrem(key,i,value)
                for value2 in r.lrange(name2 + ':' + value,0,-1):
                    # add the values of name2 klstore in name1klstore
                    r.lpush(key,value2)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    lookUp_klstore('k1','k2')
