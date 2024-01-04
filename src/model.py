import Result

class Model:
    def __init__(self, market_data):
        self.market_data = market_data
        self.n_slow = 21
        self.n_fast = 14
        # Index keeps track of where to place next price
        self.i_slow = 0
        self.i_fast = 0
        self.ewma_slow_arr = []
        self.ewma_fast_arr = []
        self.ewma_slow = 0
        self.ewma_fast = 0

    def evaluate(self):
        new_price = self.market_data.poll()
        self.eval_ewma_fast(new_price)
        self.eval_ewma_slow(new_price)

        if fast_exceeds_slow():
            return Result.BUY
        
        if fast_falls_below_slow():
            return Result.SELL
        
        else:
            return Result.NOTHING


    def eval_ewma_slow(self, new_price):
        weighted_new_price = new_price / self.n_fast
        weighted_last_price = self.ewma_slow_arr[self.i_slow] / self.n_slow
        self.ewma_slow = self.ewma_slow - weighted_last_price + weighted_new_price

    def eval_ewma_fast(self, new_price):
        weighted_new_price = new_price / self.n_fast
        weighted_last_price = self.ewma_fast_arr[self.i_fast] / self.n_fast
        self.ewma_fast = self.ewma_fast - weighted_last_price + weighted_new_price
    
    def fast_exceeds_slow()
