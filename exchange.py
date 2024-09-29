class Currency:
    def __init__(self, name, exchange_rate):
        self.name = name
        self.exchange_rate = exchange_rate

    def value_in_ducats(self, amount):
        return amount * self.exchange_rate