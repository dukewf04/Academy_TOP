from abc import abstractmethod
class Pizza:
    recipte = None
    toppings = []

    @abstractmethod
    def add_recipte(self, recipte):
        pass
    @abstractmethod
    def add_toppings(self, toppings):
        pass


class PizzaBilder(Pizza):
    def add_recipte(self, recipte):
        self.recipte = recipte
    def add_toppings(self, toppings):
        self.toppings.append(toppings)


class PizzaMenu:
    """Возвращает список всех пицц"""
    def __init__(self, builder: PizzaBilder):
        self.builder = builder
    def menuUser(self):
        menu = {
            '1': "Добро пожаловать в пиццерию",
            '2': "Только тут сможете собрать собственную пицуу",
            '3': "Выберите опцию: \n1) Своя пицца\n2) Выборка",
            '4': "Спасибо за заказ!\nОплата заказа будет в кассе"
        }

        print(menu['1'], menu['2'], menu['3'], sep='\n')
        user_value_builder = input("Сделайте выбор по заказу> ")
        self.builder.add_recipte(user_value_builder)

        user_value_toppings = int(input("Введите кол-во> "))
        for top in range(user_value_toppings):
            self.builder.add_toppings(input(f"{top} - Введите добавку> "))
        print(menu['4'])

    def menuOrder(self, payment_method):
        pass

class Order:
    """Единственный заказ"""
    def __init__(self, builder, payment_method=None):
        self.builder = builder
        self.payment_method = payment_method

class OrderHistory:
    """Логирование"""
    def __init__(self):
        self.orders = []
        self.revenue = 0
        self.profit = 0
    def add_order(self, order):
        """Создание заказа"""
        self.orders.append(order)
        self.calculate_revenue(order)
    def calculate_revenue(self, order):
        """Прибиль от заказов (с чека)"""
        self.revenue += len(order.builder.toppings)*100 + 1000
    def calculate_profit(self):
        """Профит от заказов (Общая выручка)"""
        self.profit = self.revenue*0.2
    def view_statistics(self, order):
        """Статистика заказов"""
        string_log = f"""
                    Заказ: {order.builder.recipte}
                    Ингридиенты: {order.builder.toppings}
                    Прибыль: {self.revenue}
                    Профит: {self.profit}
                    Спасибо за заказ! Приходите еще!\n
                """
        return string_log

class FileHandler:
    """Запись заказа в файл"""
    file_check = 'check.txt'
    @staticmethod
    def save_order_to_file(orders_statistics):
        with open(FileHandler.file_check, 'a', encoding='utf-8') as f:
            f.write(orders_statistics)

    @staticmethod
    def retrieve_orders_from_file():
        with open(FileHandler.file_check, 'r', encoding='utf-8') as f:
            console_value = f.read()
        print(console_value)


if __name__ == "__main__":
    pizza_builder = PizzaBilder()
    pizza_menu = PizzaMenu(pizza_builder)
    order = Order(pizza_builder)
    order_history = OrderHistory()
    FileHandler.save_order_to_file(order_history.view_statistics(order))
    FileHandler.retrieve_orders_from_file()

    pizza_menu.menuUser()
