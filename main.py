import os

from pymongo import MongoClient

print(os.environ['PATH'])

connection_string = os.environ['MONGODB_CONNECTION_STRING']
client = MongoClient(connection_string)
dbs = client.list_database_names()
print(dbs)
