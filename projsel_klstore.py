#!/usr/bin/env python3

#in case you want to delete the kl stores
#redis-cli --scan --pattern k1:* | xargs redis-cli unlink
#redis-cli --scan --pattern k2:* | xargs redis-cli unlink

import redis
import re

# define our connection information for Redis
# Replaces with your configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""

kl_store1 = {'t11':['31','62','9'], 't15':['75','91'], 't22':['55','12','112'], 't39':['44'], 't44':['42', '98']}
kl_store2 = {'t11':['12','6','95'], 't15':['128'], 't22':['43'], 't32':['39','77'], 't44':['129']}
kl_store3 = {'t11':['182'], 't16':['7','9'], 't22':['56','29'], 't38':['32','82'], 't44':['66','121','22']}

def create_klstores(name, dictionary):
    # create the Redis Connection object
    try:

        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

        #push data from dictionary in Redis
        for key,values in dictionary.items():
            nm = name + ":" + str(key)
            for v in values:
                r.lpush(nm ,str(v))

    except Exception as e:
        print(e)


def projsel_klstore(output_name, klstores_names, expression):

    # create the Redis Connection object
    try:

        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

        #We use a python dictionary in order to create the new klstore
        new_kl = {}
        for name in klstores_names:
            # get the keys in each klstore
            keys = r.keys(name + ':*')

            for key in keys:
                for value in r.lrange(key,0,-1):
                    if key[len(name) + 1:] not in new_kl:
                        #create a new array
                        new_kl[key[len(name) + 1:]] = [value]
                    else:
                        new_kl[key[len(name) + 1:]].append(value)

        #find ##keys in the expression and replace them
        expression = expression.replace("##key", "key")

        #find values in the expression
        expression_values = re.findall('##\w+', expression)

        #replace ##values in the expression
        # All values in the expression have the same name, so we choose expression_values[0]
        # For the scope of this assignment, we randomly choose the first element of each list of values.
        # For the scope of this assignment value is number and we tranfsorm it from string to integer
        expression = expression.replace(expression_values[0], "int(value[0])")
        new_kl = {key: value for key, value in new_kl.items() if eval(expression)}

        #this method transform a dictionary to klstore
        create_klstores(output_name, new_kl)


    except Exception as e:
        print(e)

if __name__ == '__main__':
    # create_klstores('ks1', kl_store1)
    # create_klstores('ks2', kl_store2)
    # create_klstores('ks3', kl_store3)
    projsel_klstore('new_klstore', ['ks1','ks2','ks3'], "##key <> 't22' and ##age > 90" )
