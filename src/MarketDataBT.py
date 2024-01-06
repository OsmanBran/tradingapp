import MarketData
from pymongo import MongoClient

class MarketDataBT(MarketData):
    def __init__(self):
        self.counter = 0

        connection_string = "mongodb://localhost:27017/"
        self.client = MongoClient(connection_string)
        self.db = self.client["local"]
        self.collection = "test_two"

    def poll(self):
        query = {"_id": self.counter}
        result = self.collection.find_one(query)

        if result:
            print("Sent item " + self.counter)
            self.counter += 1
            return result
        else:
            print("End of session")
            self.client.close()
            return None

