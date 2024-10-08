import asyncio
import websockets
import Trade
import json
from Result import Result
from datetime import datetime
from enum import Enum
## Duplicated Code - refactor pending
import time
from MarketData import MarketData
from MarketDataBT import MarketDataBT
from Position import Position
from Trade import Trade
from Model import Model
from Endpoint import Endpoint
from Exchange import Exchange
import asyncio

class MessageTypes(Enum):
     TICKER = 1
     TRADE = 2

class Server:
    def __init__(self):
        self.websocket_connections = set()
        self.sock_port = 8765
        self.sock_url = "localhost"
        self.global_socket = lambda: None
        self.sock_server = None# self.market_data: MarketData = MarketDBT()
        self.market_data: MarketData = MarketDataBT()
        self.model: Model = Model(self.market_data)
        self.endpoint = Endpoint()
        self.exchange = Exchange(Position(self.model))

    def evaluate_model(self):
        # Main logic of your program goes here
        self.market_data.poll()

        result = self.model.evaluate()
        
        if result != Result.NOTHING:
            print("Send request to ")
            self.exchange.request_trade(result)
        
        return Server.getMsg(self.market_data.last_price, self.model.ewma_fast, self.model.ewma_slow)

    def getMsg(price: float, ewma_s: float, ewma_f: float):
            msg = {
                   "message_type": MessageTypes.TICKER.name,
                   "timestamp": str(datetime.now().time()),
                   "price": price,
                   "ewma_s": ewma_s,
                   "ewma_f": ewma_f,
            }
            return json.dumps(msg)
    
    async def model_handler(self, websocket):
        while True:
            await asyncio.sleep(5)
            message = self.evaluate_model()
            print(message)
            result = await websocket.send(message)
            print(result)

    async def trade_handler(self, websocket):
        while True:
             await asyncio.sleep(1)
             trade = self.exchange.evaluate()
             if trade != None:
                json_message = {
                    "message_type": "TRADE",
                    "status": trade.status,
                    "market_Id": trade.market_Id,
                    "price": trade.price,
                    "amount": trade.amount,
                    "open_amount": trade.open_amount,
                    "type": trade.type,
                    "side": trade.side,
                    "order_Id": trade.order_Id,
                    "fiat_qty": trade.fiat_qty,
                    "total_notional": trade.total_notional,
                    "notional_change": trade.notional_change
                }
                result = await websocket.send(json.dumps(json_message))
                print(result)

    async def consumer_handler(self, websocket):
        async for message in websocket:
            print(f"Received message from client: {message}")

server = Server()

async def main(websocket, path):
    producer_task = asyncio.create_task(server.model_handler(websocket))
    trade_task = asyncio.create_task(server.trade_handler(websocket))
    await asyncio.gather(producer_task, trade_task)

start_server = websockets.serve(main, server.sock_url, server.sock_port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
