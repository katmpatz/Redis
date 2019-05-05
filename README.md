# Redis
# Key-Value Stores
###### Project for _Big Data Management Systems_ course

## Aim

Create key-value stores and implement in Python some functions/methods that get one or more KL stores and “return” (or update)
a KL store.

## How many files are included?

There are 12 files.
-3 xml files
-6 python files
-2 csvs
-1 excel

## What does each file do?

**Xml files**

The aim of xml files is to connect python with 3 data sources:

1. Csv (CSsource.xml)
2. Excel (EXsource.xml)
3. Database (DBsourse.xml)

**Csvs and excel**

The csvs and the excel are the data we use to run our project. You can create your own. The file _import to mysql.csv_ is for importing
the data to mysql database.

**create_klstore.py**

This file creates 2 klstores from 3 datasources.

**filter_klstore.py**

This file applies an expression on each element of a key list store.

**apply_klstore.py**

This file gets a KL store in Redis named <name1> and a python function and applies function on each element of a list.

**lookUp_klstore.py**

This file gets 2 klstores and transform the one with the values of the other. 

**aggr_klstore.py**

This file aggregates each list of a kl store according to the specified aggregate. 

**projSel_klstore.py**

This file joins 2 or more kl stores.

## Getting started

Would you like to install the project and run it locally? Easy-peasy! The only thing that you have to do is to follow our instructions and everything will work properly on your machine!

## Linux

The project is running on Linux.

**Installation**

Run the following commands on your terminal to install what is needed.

```
sudo apt install python-pip
pip install redis
pip install bs4
pip install lxml
pip install xlrd
pip install mysql-connector-python
git commit
```
You can use the SQL database that you want. We recommend [Mysql] (https://www.mysql.com/).

**How to run the project?**

After installing the above requirements then:

1. Clone this repository
2. Create a database in your SQL database 
3. Import the _import to mysql.csv_ in it
4. Change the file DBsource:
    - fill in the tags
        - username 	```<username>your username</username>```
        - password  ```<password>your password</password>```
        - database name ```<database> your database name```
5. To run each .py file you have to write in your terminal ```python thefilethatyouwant``` - example ```python create_klstore.py``` - in your project directory. 

**Before you run any of the .py files run the create_klstore.py file to create the klstores. After running the program, delete the kl stores and create them again to run another .py file.**

To delete the kl stores run the following commands

```redis-cli --scan --pattern k1:* | xargs redis-cli unlink```

```redis-cli --scan --pattern k2:* | xargs redis-cli unlink ``` 

Voila!!! :blush:



