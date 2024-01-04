from Result import Result
from Trade import Trade

class Position:
    def __init__(self): 
        self.fiatBalance = 5000
        self.cryptoBalance = 0
        self.startingCapital = self.fiatBalance
        self.currentOperation = Result.NOTHING

    def get_current_balance(self):
        return self.fiatBalance
    
    def get_profit_loss(self):
        return self.fiatBalance - self.startingCapital

    def subtract_balance(self, subtract_amount):
        return self.fiatBalance - subtract_amount

    def add_balance(self, add_amount):
        return self.fiatBalance + add_amount
    
    def get_trade(self, result: Result):
        if result == Result.BUY:
            quantity = 0.25 * self.fiatBalance
            trade = self.fiatBalance - quantity
            is_trade_possible = (trade > 0) & self.currentOperation != Result.BUY
            
        if result == Result.SELL:
            trade = self.fiatBalance - (0.25 * self.fiatBalance)
            is_trade_possible = trade > 0 & self.currentOperation != Result.SELL
            
        if is_trade_possible:
                trade = Trade()
                trade.market_Id: 'BTC-AUD'
                trade.amount: (trade / trade.price)
