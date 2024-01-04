import Trade
import pandas as pd

class Report:
    def __init__(self):
        self.trade_historical = []

    def record_trade(self, trade: Trade):
        self.trade_historical.append(trade)
    
    def generate_report(self):
        data = [{"price": trade.price, "amount": trade.amount, "side": trade.side, "fiat_balance": trade.fiat_balance} for trade in self.trade_historical]