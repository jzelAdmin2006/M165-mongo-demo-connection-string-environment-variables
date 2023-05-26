import os

from db import Db

print(os.environ['PATH'])

db = Db()
client = db.get_client()
dbs = client.list_database_names()
print(dbs)
