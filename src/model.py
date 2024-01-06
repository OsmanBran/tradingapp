import Result

class Model:
    def __init__(self, market_data):
        self.market_data = market_data
        self.new_price = 0
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
        # If ewma is the same, skip this evaluation, order has already been bought or sold.
        if self.ewma_slow == self.ewma_fast:
            return

        prev_state = self.ewma_slow > self.ewma_fast
        self.new_price = self.market_data.poll()
        self.eval_ewma_fast(self.new_price)
        self.eval_ewma_slow(self.new_price)
        new_state = self.ewma_slow >= self.ewma_fast

        if Model.fast_exceeds_slow(prev_state, new_state):
            return Result.BUY
        
        if Model.slow_exceeds_fast(prev_state, new_state):
            return Result.SELL
        
        else:
            return Result.NOTHING

    def fast_exceeds_slow(prev_state, new_state):
        # State true if slow higher than fast.
        # Fast exceeded if slow was higher but is now lower.
        return prev_state and not new_state

    def slow_exceeds_fast(prev_state, new_state):
        # State true if slow higher than fast.
        # Slow exceeds if slow was lower but is now higher.
        return not prev_state and new_state

    def eval_ewma_slow(self, new_price):
        weighted_new_price = new_price / self.n_fast
        weighted_last_price = self.ewma_slow_arr[self.i_slow]
        self.ewma_slow = self.ewma_slow - weighted_last_price + weighted_new_price
        self.ewma_slow_arr[self.i_slow] = weighted_new_price

    def eval_ewma_fast(self, new_price):
        weighted_new_price = new_price / self.n_fast
        weighted_last_price = self.ewma_fast_arr[self.i_fast]
        self.ewma_fast = self.ewma_fast - weighted_last_price + weighted_new_price
        self.ewma_fast_arr[self.i_fast] = weighted_new_price