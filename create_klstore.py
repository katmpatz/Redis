#!/usr/bin/env python3

#in case ou want to delete the kl stores
#redis-cli --scan --pattern k1:* | xargs redis-cli unlink
#redis-cli --scan --pattern k2:* | xargs redis-cli unlink

'''
    Before running the program you have to install:
    redis
    bs4
    lxml
    pandas
    mysql-connector-python
'''
import redis
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector
from mysql.connector import Error

# define our connection information for Redis
# Replaces with your configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""


def create_KLStore_excel (name, data_source, query_string, position1, position2, direction):

    # create the Redis Connection object
    try:

        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

        # open the data_source
        infile = open(data_source)

        # read the data_source
        contents = infile.read()

        #get the xml
        soup = BeautifulSoup(contents,'xml')

        #get the text that is in filename tag
        file = soup.find('filename').text

        #read the excel file
        df = pd.read_excel(file, query_string)

        #push data in the right Redis list
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

    # create the Redis Connection object
    try:
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

        # open the data_source
        infile = open(data_source)

        # read the data_source
        contents = infile.read()

        # get the xml
        soup = BeautifulSoup(contents,'xml')

        # get the text that is in filename tag
        file = soup.find('filename').text

        # read the csv file
        df = pd.read_csv(file)

        #push data in the right Redis list
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

def create_KLStore_db (name, data_source, query_string, position1, position2, direction):

    # create the Redis Connection object
    try:
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

        # open the data_source
        infile = open(data_source)

        # read the data_source
        contents = infile.read()

        # get the xml
        soup = BeautifulSoup(contents,'xml')

        # # get the text that is in username, password and database tags
        username = soup.find('username').text
        password = soup.find('password').text
        database = soup.find('database').text

        # connect to mySQL
        mySQLconnection = mysql.connector.connect(user=username, password=password,
                              host='localhost',
                              database=database)

        # execute the query and get the records
        cursor = mySQLconnection .cursor()
        cursor.execute(query_string)
        records = cursor.fetchall()

        # push each row in the right Redis list
        if direction == 1:
            for row in records:
                nm = name+":"+ str(row[0])
                r.lpush(nm ,str(row[1]))
        elif direction == 2:
            for row in records:
                nm = name+":"+ str(row[1])
                r.lpush(nm,str(row[0]))

    except Error as e :
        print ("Error while connecting to MySQL", e)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    create_KLStore_excel("k1","EXsource.xml","Sheet1",1,2,1)
    create_KLStore_excel("k2","EXsource.xml","Sheet1",1,2,2)
    create_KLStore_csv("k2","CSsource.xml",None,1,2,2)
    create_KLStore_csv("k1","CSsource.xml",None,1,2,1)
    create_KLStore_db ("k1", "DBsource.xml", 'SELECT * FROM cust_transactions', None,None, 1)
    create_KLStore_db ("k2", "DBsource.xml", 'SELECT * FROM cust_transactions', None,None, 2)
