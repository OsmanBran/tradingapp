class Trade:
    def __init__(self):
        self.status = None # Accepted/Filled etc.
        self.market_Id = "INVALID"
        self.price = 0.0
        self.amount = 0.0
        self.open_amount = 0.0
        self.type = "Market" # string (OrderType) Enum: "Limit" "Market" "Stop Limit" "Stop" "Take Profit"
        self.side = "Ask"
        self.fiat_qty = 0
        self.order_Id = 0
        self.total_notional = 0.0
        self.notional_change = 0
