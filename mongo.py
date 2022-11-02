from pymongo import MongoClient

class DB:
    
    def get_database():
        CONNECTION_STRING = "<todo>"

        client = MongoClient(CONNECTION_STRING)
        barcode = client['barcode']
        return barcode["iter_one"]

    def get_items(self, id):

        return self.find({"_id": id})

    def insert_items(self, items):
        if items.len < 1:
            return

        else if items.len <2:
            self.insert_one(items)

        else :
            self.insert_many(items)
