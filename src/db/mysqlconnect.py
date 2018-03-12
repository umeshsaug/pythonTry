#!/usr/bin/python3

# to install mysql connector us following command with pip3 
# pip install mysql-connector-python

import mysql.connector

'''
# Open database connection
db = PyMySQL.connect("103.14.99.155","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()
'''

#  cnx = mysql.connector.connect(user='root', password='V$rt0z@1234', host='103.14.99.155', database='sys', use_pure=False)


config = {
  'user': 'root',
  'password': 'V$rt0z@1234',
  'host': '103.14.99.155',
  'database': 'sys',
  'raise_on_warnings': True,
  'use_pure': False,
}

cnx = mysql.connector.connect(**config)

cnx.close()
