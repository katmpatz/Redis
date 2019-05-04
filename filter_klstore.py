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


def filter_klstore (name1, expression):

    # create the Redis Connection object
    try:

        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

        # get the keys in name1 klstore
        keys = r.keys(name1 + ':*')

        # get each key of keys
        for key in keys:
            # i is for index in list
            i = -1
            # get every value of key
            for value in r.lrange(key,0,-1):
                i = i + 1
                if not (eval(expression)):
                    r.lrem(key,i,value)

    except Exception as e:
        print(e)

if __name__ == '__main__':

    filter_klstore('k1','len(value) < 1')
    filter_klstore('k2','len(value) < 2')
