from MarketData import MarketData
from pymongo import MongoClient

class MarketDataBT(MarketData):
    def __init__(self):
        self.counter = 0
        connection_string = "mongodb+srv://globalAccess:osmi1234@crypto-db.2egqfjz.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(connection_string)
        self.db = self.client["Crypto-DB"]
        self.collection = self.db["BTC-Collection-Test-7"]
        self.last_price = 0
        self.max = 70

    def poll(self):
        query = {"_id": self.counter}
        result = self.collection.find_one(query)

        if result:
            print("Sent item " + str(self.counter))
            self.counter += 1
            self.last_price = float(result["lastPrice"])
        else:
            print("No item found for " + str(self.counter))
    def close(self):
        self.client.close()
        
        

