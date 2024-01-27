import Trade
import json
import copy
from Result import Result
from enum import Enum
from queue import Queue

class Eval_Type(Enum):
    REQUEST = 0
    ACCEPTED = 1
    FILL = 2

class Exchange:
    def __init__(self, position):
        # stores a tuple of (EVAL_TYPE, Data). Possible combinations:
        # (REQUEST, Result(Buy/Sell))
        self.position = position
        self.evaluation_queue = Queue()
        self.mock_order_id = 1

    def request_trade(self, result: Result):
        self.evaluation_queue.put((Eval_Type.REQUEST, result))

    def evaluate_request(self, result: Result):
        trade: Trade = self.position.get_trade(result)
        if (trade != None):
            print(f"Trade request {result} was approved from position")
            self.post_trade(trade)
        else:
            print(f"Trade request {result} was rejected from position")
    
        # No need to post on GUI until exchange received.
        return None

    def post_trade(self, trade: Trade):
        print("Sending trade to exchange")
        # here we just mock the exchange sending accepted trade back to us
        # remove this block later.
        trade.status = Eval_Type.ACCEPTED.name
        trade.open_amount = trade.amount    
        trade.orderId = self.mock_order_id
        self.mock_order_id += 1
        self.evaluation_queue.put((Eval_Type.ACCEPTED, trade))

    def evaluate_accepted(self, trade: Trade):
        print("Trade accepted")
        # here we mock exchange filling order after accept.
        # remove this block later.
        mock_filled_trade = copy.deepcopy(trade)
        mock_filled_trade.status = "FILLED"
        mock_filled_trade.open_amount = 0.0
        self.evaluation_queue.put((Eval_Type.FILL, mock_filled_trade))
        
        return trade
    
    def evaluate_fill(self, trade: Trade):
        print("Trade filled")
        return trade

    def evaluate(self):
        # step 1. Poll exchange for latest updates.
        # todo. 

        # step 2. Evaluate state
        if self.evaluation_queue.empty():
            return
        
        output = None
        eval_type, eval_body = self.evaluation_queue.get()
        if (eval_type == Eval_Type.REQUEST):
            output = self.evaluate_request(eval_body)
        if (eval_type == Eval_Type.ACCEPTED):
            output = self.evaluate_accepted(eval_body)
        if (eval_type == Eval_Type.FILL):
            output = self.evaluate_fill(eval_body)
        
        # step 3. Publish position changes
        return output