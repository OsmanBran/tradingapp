class Trade:
    def __init__(self):
        self.status # Accepted/Filled etc.
        self.market_Id
        self.price
        self.amount = 0.0
        self.open_amount = 0.0
        self.type # string (OrderType) Enum: "Limit" "Market" "Stop Limit" "Stop" "Take Profit"
        self.side
        self.fiat_balance
        self.order_Id = 0
