import time
from MarketData import MarketData
from MarketDataBT import MarketDataBT
from Position import Position
from Trade import Trade
from Model import Model
from Endpoint import Endpoint
import asyncio

# This is deprecated now.
class MainClass:
    def __init__(self):
        self.market_data: MarketData = MarketDataBT()
        self.model: Model = Model(self.market_data)
        self.position = Position(self.model)
        self.endpoint = Endpoint()

    async def main_loop(self):
        # start websocket
        await self.endpoint.start_server()

        while True:
            # Main logic of your program goes here
            self.market_data.poll()
            result = self.model.evaluate()
            
            trade: Trade = self.position.get_trade(result)
            
            await self.endpoint.broadcast(self.market_data.last_price, self.model.ewma_fast, self.model.ewma_slow, self.position.fiat_balance, trade)

            # Wait for 1 second before the next iteration
            time.sleep(1)

async def main():
    main_instance = MainClass()

    # Call the main loop to start the program
    await main_instance.main_loop()

asyncio.get_event_loop().run_until_complete(main())