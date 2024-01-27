import time
import requests

class MarketData:
    def __init__(self):
        self.url = "https://api.btcmarkets.net/v3/markets/BTC-AUD/ticker"
        self.last_price = 0

    def poll(self):
        response = requests.get(self.url)
        
        if response.status_code == 200:
            data = response.json()
            
            self.last_price = float(data['lastPrice'])
            print("MARKET DATA", data, self.last_price)
        else:
            print(f"Error: {response.status_code}")

# # Fetch and print BTC/USDT data
# btc_usdt_data = fetch_btc_usdt_data()

# api_key = 'add api key here'
# private_key = 'y2a1GN8z6/etsLHo96VH+LgwHdSE92RbMK2eiNoV1i4t0x8tmuV0WYPsilPOwFBTtsIrZ7TSgq62s0zXH98vPg=='

# client = BTCMarkets(api_key, private_key)
# print(btc_usdt_data)