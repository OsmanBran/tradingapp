import time
import datetime
import requests
import argparse
from pymongo import MongoClient
from pymongo.server_api import ServerApi

class BacktestDb:
    def __init__(self):
        connection_string = "mongodb+srv://globalAccess:osmi1234@crypto-db.2egqfjz.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(connection_string, server_api=ServerApi('1'))
        self.db = self.client["Crypto-DB"]
        self.collection = None

        self.url = "https://api.btcmarkets.net/v3/markets/BTC-AUD/ticker"

    
    def start_session(self, collection_str: str, interval_minutes: int, session_length: int):
        self.collection = self.db[collection_str]
                
        session_count = int( session_length / interval_minutes )
        
        for i in range(session_count):
            response = requests.get(self.url)
            
            if response.status_code == 200:
                data = response.json()
                data["_id"] = i
                self.push_update(data)
                print(data)            
            else:
                print(f"Error: {response.status_code}")

            time.sleep(interval_minutes * 60)
        print("Session complete saved to db ...")
    
    def push_update(self, data):
        self.collection.insert_one(data)

def main():
    parser = argparse.ArgumentParser(description='Download data from btc markets')
    parser.add_argument('--interval', '-i', default=1, help='Interval between data in minutes')
    parser.add_argument('--length', '-l', default=30, help='Length of the session in minutes')
    args = parser.parse_args()

    print("Interval (minutes):", args.interval)
    print("Session Length (minutes):", args.length)

    # collection is named in format YYYYMMDD-HH-MM-SS
    current_datetime = datetime.datetime.now()
    collection_str = current_datetime.strftime("%Y%m%d-%H%M%S")
    print("Storing to collection:", collection_str)

    db = BacktestDb()
    db.start_session(collection_str, args.interval, args.length)

if __name__ == "__main__":
    main()