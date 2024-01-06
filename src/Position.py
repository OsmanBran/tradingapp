from MarketData import MarketData
from Result import Result
from Trade import Trade
from Model import Model

class Position:
    def __init__(self, model: Model): 
        self.fiat_balance = 5000
        self.cryptoBalance = 0
        self.startingCapital = self.fiat_balance
        self.currentOperation = Result.NOTHING
        self.new_price = model.new_price
        self.is_trade_possible: bool = 0

    def get_current_balance(self):
        return self.fiat_balance
    
    def get_profit_loss(self):
        return self.fiat_balance - self.startingCapital

    def subtract_balance(self, subtract_amount):
        return self.fiat_balance - subtract_amount

    def add_balance(self, add_amount):
        return self.fiat_balance + add_amount
    
    def get_trade(self, result: Result):
        if result == Result.BUY:
            quantity = 0.25 * self.fiat_balance
            requested_trade = self.fiat_balance - quantity
            self.is_trade_possible = (trade > 0) & (self.currentOperation != Result.BUY)
            
        if result == Result.SELL:
            requested_trade = self.fiat_balance - (0.25 * self.fiat_balance)
            self.is_trade_possible = (requested_trade > 0) & (self.cryptoBalance > 0) & (self.currentOperation != Result.SELL)
            
        if self.is_trade_possible:
            trade = Trade()
            trade.market_Id: 'BTC-AUD'
            trade.price: self.new_price
            trade.amount: (requested_trade / self.new_price)
            trade.type: 'Limit' # TODO: Change to Limit eventually
            trade.side: 'Bid' if result == Result.BUY else 'Ask'
            trade.fiat_balance: self.fiat_balance
            
            return trade
                

