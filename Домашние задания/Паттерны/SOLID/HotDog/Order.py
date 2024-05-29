from HotDog import HotDog
from FoodStore import FoodStore

class Order:
    """Класс отвечающий за заказы пользователей, расчет стоимости"""
    def __init__(self, store: FoodStore):
        self.store = store
        self.count = 0
        self.discount = 0
        self.total_cost = 0
        self.order_description = {}

    def add_hotdog(self, hotdog: dict):
        if self.store.check_components(hotdog["components"]):
            self.count += 1
            self.total_cost += hotdog["cost"]
            self.order_description[hotdog["title"]] += 1 if hotdog["title"] in self.order_description.keys() else 1
            for el in hotdog["components"]:
                self.store.get_component(el)

            return True

        return False


    def get_order(self):
        """Получить итоговую информацию о заказе"""

        self.discount = self.count // 3  # %
        self.total_cost -= self.discount/100
        self.order_description["Скидка"] = self.discount
        self.order_description["Итоговая стоимость"] = self.total_cost
