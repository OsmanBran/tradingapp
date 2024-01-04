import time

class MainClass:
    def __init__(self):
        # Initialization code, if needed
        pass

    def main_loop(self):
        while True:
            # Main logic of your program goes here
            print("Hello, this is the main class!")

            # Wait for 1 second before the next iteration
            time.sleep(1)

if __name__ == "__main__":
    # Create an instance of the MainClass
    main_instance = MainClass()

    # Call the main loop to start the program
    main_instance.main_loop()