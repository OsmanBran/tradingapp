from MarketData import MarketData
from pymongo import MongoClient

class MarketDataBT(MarketData):
    def __init__(self):
        self.counter = 0

        connection_string = "mongodb+srv://globalAccess:osmi1234@crypto-db.2egqfjz.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(connection_string)
        self.db = self.client["Crypto-DB"]
        self.collection = self.db["BTC-Collection"]
        self.last_price = 0
        self.max = 70

    def poll(self):
        query = {"_id": self.counter}
        result = self.collection.find_one(query)

        if self.counter == self.max: self.counter = 0

        if result:
            print("Sent item " + str(self.counter))
            self.counter += 1
            self.last_price = float(result["lastPrice"])
        else:
            print("End of session")
            self.client.close()

