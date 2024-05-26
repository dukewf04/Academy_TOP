class Order:
    def __init__(self):
        self.total_sales = 0
        self.revenue = 0
        self.profit = 0

    def add_order(self, summa):
        self.total_sales += 1
        self.revenue += summa
        self.profit = self.revenue * 0.7