import os

from pymongo import MongoClient


class Db:
    def __int__(self):
        self.client = MongoClient(os.environ['MONGODB_CONNECTION_STRING'])

    def get_client(self):
        return self.client
