import time
from MarketData import MarketData
from Position import Position
from model import Model

class MainClass:
    def __init__(self):
        self.model = Model()

    def main_loop(self):
        while True:
            # Main logic of your program goes here

            data = MarketData()

            data.poll(1)
            # result = self.model.evaluate()
            
            # Position.get_trade(result)

            
            # Wait for 1 second before the next iteration
            time.sleep(1)

if __name__ == "__main__":
    # Create an instance of the MainClass
    main_instance = MainClass()

    # Call the main loop to start the program
    main_instance.main_loop()