import asyncio
import websockets
import Trade
import json
from datetime import datetime
from TempProducer import TempProducer
## Duplicated Code - refactor pending
import time
from MarketData import MarketData
from MarketDataBT import MarketDataBT
from Position import Position
from Trade import Trade
from Model import Model
from Endpoint import Endpoint
import asyncio

class TempServer:
    def __init__(self):
        self.websocket_connections = set()
        self.sock_port = 8765
        self.sock_url = "192.168.1.121"
        self.global_socket = lambda: None
        self.sock_server = None

        self.market_data: MarketData = MarketDataBT()
        self.model: Model = Model(self.market_data)
        self.position = Position(self.model)
        self.endpoint = Endpoint()

    def producer(self):
        # Main logic of your program goes here
        self.market_data.poll()
        result = self.model.evaluate()
        
        trade: Trade = self.position.get_trade(result)
        
        return TempServer.getMsg(self.market_data.last_price, self.model.ewma_fast, self.model.ewma_slow, self.position.fiat_balance, trade)

    def getMsg(price: float, ewma_s: float, ewma_f: float, balance: float, trade: Trade):
            msg = {
                   "timestamp": str(datetime.now().time()),
                   "price": price,
                   "ewma_s": ewma_s,
                   "ewma_f": ewma_f,
                   "balance": balance,
                   "trade": trade
            }
            return json.dumps(msg)
    
    async def producer_handler(self, websocket):
        while True:
            await asyncio.sleep(5)
            message = self.producer()
            print(message)
            result = await websocket.send(message)
            print(result)

    async def consumer_handler(self, websocket):
        async for message in websocket:
            print(f"Received message from client: {message}")


    async def broadcast(self, price: float, ewma_s: float, ewma_f: float, balance: float, trade: Trade):
            msg = {
                   "timestamp": str(datetime.now().time()),
                   "price": price,
                   "ewma_s": ewma_s,
                   "ewma_f": ewma_f,
                   "balance": balance,
                   "trade": trade
            }
            json_str = json.dumps(msg)
            print("sending msg: " + json_str)

            # Broadcast the message to all connected clients
            await asyncio.gather(*[client.send(json_str) for client in self.websocket_connections])


server = TempServer()

async def main(websocket, path):
    producer_task = asyncio.create_task(server.producer_handler(websocket))
    consumer_task = asyncio.create_task(server.consumer_handler(websocket))
    await asyncio.gather(producer_task, consumer_task)

start_server = websockets.serve(main, server.sock_url, server.sock_port)
    
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
