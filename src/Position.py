class Position:
    def __init__(self): 
        self.balance = 5000
        self.currentPosition = 0
        self.startingCapital = self.balance

    def get_current_balance(self):
        return self.balance
    
    def get_profit_loss(self):
        return self.balance - self.startingCapital

    def subtract_balance(self, subtract_amount):
        return self.balance - subtract_amount

    def add_balance(self, add_amount):
        return self.balance + add_amount
    
    def get_trade(self, result):
        if result.Buy:
            trade = self.balance - (0.25 * self.balance)
            is_trade_possible = trade > 0

            
            if is_trade_possible:
                Trade.Buy
        
        if result.Sell:
            trade = self.balance + (0.25 * self.balance)
            is_trade_possible = trade > 0
            
            if is_trade_possible:
                Trade.Buy
