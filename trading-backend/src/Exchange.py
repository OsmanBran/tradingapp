import Trade

class Exchange:
    def __init__(self, name):
        self.trade_historical = []

    def post_trade(self, trade: Trade):
        self.trade_historical.append(trade)