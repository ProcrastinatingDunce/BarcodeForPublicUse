from pymongo import MongoClient


class DB:
    def __init__(connection_string):
        self.connection_string = connection_string

    
    def get_database():
        CONNECTION_STRING = self.connection_string

        client = MongoClient(CONNECTION_STRING)
        barcode = client['barcode']
        return barcode["iter_one"]

    def get_items(self, id):

        return self.find({"_id": id})

    def insert_items(self, items):
        try:
            else if items.len <2:
                 self.insert_one(items)

            else :
                self.insert_many(items)
        except:
            return 404
