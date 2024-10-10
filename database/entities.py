class User:
    def __init__(self, nickname:str, email:str, password:str):
        self.nickname = nickname
        self.email = email
        self.password = password

class Message:
    def __init__(self, sender:str, receiver:str, content:str):
        self.sender = sender
        self.receiver = receiver
        self.content = content

