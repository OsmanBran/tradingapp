import asyncio
import websockets
import Trade
import json
from datetime import datetime

class Endpoint:
    def __init__(self):
        self.websocket_connections = set()
        self.sock_port = 8765
        self.sock_url = "192.168.1.121"
        self.global_socket = lambda: None
        self.sock_server = None

    async def start_server(self):
        self.sock_server = websockets.serve(self.register, self.sock_url, self.sock_port)
        await asyncio.sleep(0.3) # Start up time

    async def register(self, websocket):
        print('register event received')
        self.websocket_connections.add(websocket) # Add this client's socket

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
