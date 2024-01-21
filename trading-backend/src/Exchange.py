import Trade
import json
from queue import Queue

class Exchange:
    def __init__(self):
        self.pending_orders = Queue()
        self.accepted_orders = Queue()
        self.mock_order_id = 1

    def poll_trades(self):
        # post any pending trades
        if not self.pending_orders.empty():
            print("Mark order as sent to exchange")
            # mock order successful acceptance
            trade = self.pending_orders.get()
            self.accepted_orders.put(trade)
            self.orderId = self.mock_order_id
            self.mock_order_id += 1
            return trade
        
        # poll for any trade updates on pending orders
        if not self.accepted_orders.empty():
            print("Mark order as filled by exchange")
            trade = self.accepted_orders.get()
            trade.status = "Filled"
            trade.open_amount = 0.0
            return trade
        
        return None

    def post_trade(self, trade: Trade):
        self.pending_orders.put(trade)

        ## pretend to send order here and we get something back. Note should run on separate thread later.
        trade.status = "Accepted"
        trade.open_amount = trade.amount
