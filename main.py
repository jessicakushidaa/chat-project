from database.mongohandler import MongoHandler

if __name__ == '__main__':
        handler = MongoHandler()
        auth = handler.authenticate("naah.sumida@gmail.com", "chatpy123")

        print(auth)

