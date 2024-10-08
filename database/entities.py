class User:
    def __init__(self, nickname:str, email:str, password:str):
        self.nickname = nickname
        self.email = email
        self.password = password

class Message:
    def __init__(self, sender:str, recipient:str, content:str):
        self.sender = sender
        self.recipient = recipient
        self.content = content

