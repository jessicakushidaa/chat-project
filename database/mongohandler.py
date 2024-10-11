from typing import List, Type

from numpy.ma.core import append
from pymongo import MongoClient
from database.entities import Message, User


class MongoHandler:
    def __init__(self):
        self.client = MongoClient('mongodb+srv://jessicakushida2:chatpy123@chat-python.ex2ps.mongodb.net/')

    def connect(self, database_name):
        return self.client[database_name]

    def authenticate (self, user:User) -> bool:
        db = self.connect("chat-python")
        user = db.users.find_one({"email": user.email, "password": user.password})
        if user:
            return True
        else:
            return False


    def get_messages (self, email) -> List[Message]:
        db = self.connect("chat-python")
        response = []
        messages = db.messages.find({"receiver": email})
        for message in messages:
            response.append(Message(sender=message["sender"],receiver= message["receiver"], content=message["content"]))
        return response

    def insert_message (self, message: Message) -> bool:
        db = self.connect("chat-python")
        message = Message(sender=message.sender,receiver=message.receiver, content=message.content)
        message_id = db.messages.insert_one({
          "sender": message.sender,
          "receiver": message.receiver,
          "content": message.content
        }).inserted_id
        if message_id: return True

        return False


