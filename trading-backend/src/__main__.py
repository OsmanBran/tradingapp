import time
import MarketData
import MarketDataBT
import Position
from Trade import Trade
from Model import Model

class MainClass:
    def __init__(self):
        self.market_data: MarketData = MarketDataBT()
        self.model: Model = Model(self.market_data)
        self.position = Position(self.model)

    def main_loop(self):

        while True:
            # Main logic of your program goes here
            self.market_data.poll()
            result = self.model.evaluate()
            print('result!!1', result)
            
            trade: Trade = self.position.get_trade(result)
            
            print('TRADE OBJECT', trade)

            
            # Wait for 1 second before the next iteration
            time.sleep(1)

if __name__ == "__main__":
    # Create an instance of the MainClass
    main_instance = MainClass()

    # Call the main loop to start the program
    main_instance.main_loop()