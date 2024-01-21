from MarketData import MarketData
from Result import Result
from Trade import Trade
from Model import Model

class Position:
    def __init__(self, model: Model): 
        self.fiat_qty = 5000
        self.crypto_qty = 0
        self.starting_qty = self.fiat_qty
        self.model = model

    def get_current_profit(self):
        return self.fiat_qty - self.starting_qty
    
    def get_trade(self, result: Result):
        if result == Result.NOTHING:
            return None

        trade_notional = 0
        if result == Result.BUY:
            # to do listen for exchange confirm
            trade_notional = 0.25 * self.fiat_qty
            self.fiat_qty -= trade_notional
            trade_qty = (trade_notional / self.model.new_price)
            self.crypto_qty += trade_qty
            
            total_notional = self.fiat_qty + self.crypto_qty * self.model.new_price
            print(f"BUY: Price: {self.model.new_price}, Qty: {trade_qty}, Total Notional: {total_notional}")

            trade = Trade()
            trade.market_Id: "BTC-AUD"
            trade.price: self.model.new_price
            trade.amount: trade_qty
            trade.type: "Market" # TODO: Change to Limit eventually
            trade.side: "Bid"
            trade.fiat_qty: self.fiat_qty
            return trade
            
        if result == Result.SELL and self.crypto_qty > 0:
            print("SELL: Price: %d, Qty: %d, Total Notional: %d")

            # to do listen for exchange confirm
            self.fiat_qty += self.crypto_qty * self.model.new_price
            self.crypto_qty = 0

            total_notional = self.fiat_qty + self.crypto_qty * self.model.new_price
            print(f"SELL: Price: {self.model.new_price}, Qty: {self.crypto_qty}, Total Notional: {total_notional}")


            trade = Trade()
            trade.market_Id: "BTC-AUD"
            trade.price: self.model.new_price
            trade.amount: self.crypto_qty
            trade.type: "Market" # TODO: Change to Limit eventually
            trade.side: "Ask"
            trade.fiat_qty: self.fiat_qty
            return trade

        return None
                

