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
3. Database (DBxourse.xml)

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

