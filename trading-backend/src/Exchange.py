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
        trade = self.pending_orders.get()
        if trade != None:
            # mock order successful acceptance
            self.accepted_orders.put(trade)
            self.orderId = self.mock_order_id
            self.mock_order_id += 1
            return trade
        
        # poll for any trade updates on pending orders
        trade = self.accepted_orders.get()
        if trade != None:
            trade.status = "Filled"
            trade.open_amount = 0.0
            return trade
        
        return None

    def post_trade(self, trade: Trade):
        self.pending_orders.put(trade)

        ## pretend to send order here and we get something back. Note should run on separate thread later.
        trade.status = "Accepted"
        trade.open_amount = trade.amount
    
    def getTradeMsg( trade: Trade):
        msg = {
                "message_type": "TRADE",
                "status": trade.status,
                "market_Id": trade.market_Id,
                "price": trade.price,
                "amount": trade.amount,
                "open_amount": trade.open_amount,
                "type": trade.type,
                "side": trade.side,
                "fiat_balance": trade.fiat_balance,
                "order_Id": trade.order_Id
        }
        return json.dumps(msg)
