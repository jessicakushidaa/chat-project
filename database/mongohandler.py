from pymongo import MongoClient
from database.entities import Message

class MongoHandler:
    def __init__(self):
        self.client = MongoClient('mongodb+srv://jessicakushida2:chatpy123@chat-python.ex2ps.mongodb.net/', )