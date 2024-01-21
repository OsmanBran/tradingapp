import time
import requests
from pymongo import MongoClient
from pymongo.server_api import ServerApi

class BacktestDb:
    def __init__(self):
        connection_string = "mongodb+srv://globalAccess:osmi1234@crypto-db.2egqfjz.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(connection_string, server_api=ServerApi('1'))
        self.db = self.client["Crypto-DB"]
        self.collection = None
        self.interval_seconds = 30
        self.counter = 0
        self.url = "https://api.btcmarkets.net/v3/markets/BTC-AUD/ticker"

    
    def start_session(self, collection_str: str, interval_seconds: int):
        self.collection = self.db[collection_str]
        self.interval_seconds = interval_seconds
        self.counter = 0
        
        while True:
            response = requests.get(self.url)
            
            if response.status_code == 200:
                data = response.json()
                data["_id"] = self.counter
                self.counter += 1
                self.push_update(data)
                print(data)            
            else:
                print(f"Error: {response.status_code}")

            time.sleep(self.interval_seconds)
    
    def push_update(self, data):
        self.collection.insert_one(data)

test_str = {
"marketId": "BAT-AUD",
"bestBid": "0.2612",
"bestAsk": "0.2677",
"lastPrice": "0.2652",
"volume24h": "6392.34930418",
"volumeQte24h": "1.39",
"price24h": "130",
"pricePct24h": "0.002",
"low24h": "0.2621",
"high24h": "0.2708",
"timestamp": "2019-09-01T10:35:04.940000Z"
}

testDb = BacktestDb()
testDb.start_session("BTC-Collection-Test-1", 30)
