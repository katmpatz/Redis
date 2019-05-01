#!/usr/bin/env python3

#redis-cli --scan --pattern users:* | xargs redis-cli unlink

# step 1: import the redis-py client package
import redis
from bs4 import BeautifulSoup
import pandas as pd

# step 2: define our connection information for Redis
# Replaces with your configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""


def create_KLStore_excel (name, data_source, query_string, position1, position2, direction):

    # step 3: create the Redis Connection object
    try:

        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

        infile = open(data_source)
        contents = infile.read()
        soup = BeautifulSoup(contents,'xml')
        file = soup.find('filename').text
        df = pd.read_excel(file, query_string)
        #print(df.ix[0,0])
        if direction == 1:
            for index,i in df.iterrows():
                nm = name+":"+ str(i[position1 - 1])
                r.lpush(nm ,str(i[position2 - 1]))
        elif direction == 2:
            for index,i in df.iterrows():
                nm = name+":"+ str(i[position2 - 1])
                r.lpush(nm,str(i[position1 - 1]))

    except Exception as e:
        print(e)

def create_KLStore_csv (name, data_source, query_string, position1, position2, direction):

    # step 3: create the Redis Connection object
    try:
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

        infile = open(data_source)
        contents = infile.read()
        soup = BeautifulSoup(contents,'xml')
        file = soup.find('filename').text
        df = pd.read_csv(file)
        if direction == 1:
            for index,i in df.iterrows():
                nm = name+":"+ str(i[position1 - 1])
                r.lpush(nm ,str(i[position2 - 1]))
        elif direction == 2:
            for index,i in df.iterrows():
                nm = name+":"+ str(i[position2 - 1])
                r.lpush(nm,str(i[position1 - 1]))

    except Exception as e:
        print(e)

if __name__ == '__main__':
    #create_KLStore_excel("k1","EXsource.xml","Sheet1",1,2,1)
    #create_KLStore_excel("k2","EXsource.xml","Sheet1",1,2,2)
    #create_KLStore_csv("k2","CSsource.xml",None,1,2,2)
    #create_KLStore_csv("k1","CSsource.xml",None,1,2,1)
