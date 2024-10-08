from pymongo import MongoClient
from database.entities import Message

class MongoHandler:
    def __init__(self):
        self.client = MongoClient('mongodb+srv://jessicakushida2:chatpy123@chat-python.ex2ps.mongodb.net/')

    def connect(self, database_name):
        return self.client[database_name]

    def authenticate (self, email, password) -> bool:
        db = self.connect("chat-python")
        user = db.users.find_one({"email": email, "password": password})
        if user:
            return True
        else:
            return False



