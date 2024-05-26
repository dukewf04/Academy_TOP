from Model.HotDog import HotDog

class Statistic:
    """Класс для хранения информации по проданным хотдогам, выручке, прибыли.
    Так же в этом классе хранится информация по скидке на покупку от 3 хотдогов.
    """

    total_count = 0
    revenue = 0
    profit = 0
    discount_percent = 0.05  # Начальная скидка от 3 хотдогов в

    @staticmethod
    def buy_hotdog():
        Statistic.total_count += 1

    @staticmethod
    def calculate_profit(cost_for_hotdog):
        Statistic.revenue += cost_for_hotdog
        Statistic.profit += Statistic.revenue * 0.2

    @staticmethod
    def calculate_discount(count_hotdog: int):
        discount = Statistic.discount_percent * (count_hotdog // 3)
        return discount
