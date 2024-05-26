import sys
from Model.Pizza import Pizza
from Order import Order

class View:
    def __init__(self):
        self.order = Order()

    def main_menu(self):
        while True:
            menu = """
                Главное меню:
                1. Заказать пиццу
                2. Статискика по проданным пиццам
                3. Выход"""
            print(menu)
            choice = int(input("> "))
            if choice == 3:
                print("Всего хорошего!")
                sys.exit(0)

            if choice == 1:
                self.check_pizza()
            else:
                self.show_statistic()


    def check_pizza(self):
        print("Выберите пиццу")
        for i, el in enumerate(Pizza.pizza_list):
            print(f"[{i+1}] {el['title']}, цена {el['price']} руб.")
        pizza_choice = int(input("> "))

        print("Выберите топпинг для пиццы")
        for i, el in enumerate(Pizza.toppings):
            print(f"[{i+1}] {el['title']}, цена {el['price']} руб.")
        print("[0] - без топпига")
        topping_choice = int(input("> "))

        total_cost = Pizza.pizza_list[pizza_choice-1]['price']
        if topping_choice != 0:
            total_cost += Pizza.toppings[topping_choice-1]['price']
            order = f"Ваш заказ:\nПицца: {Pizza.pizza_list[pizza_choice - 1]['title']}\nТоппинг: {Pizza.toppings[topping_choice - 1]['title']}\nИтоговая цена: {total_cost}"
        else:
            order = f"Ваш заказ:\nПицца: {Pizza.pizza_list[pizza_choice - 1]['title']}\nИтоговая цена: {total_cost}"
        self.order.add_order(total_cost)

        print(order)
        oplata = input("Оплатите [1] - наличные, [2] по карте> ")

        with open('orders.txt', 'a', encoding='utf-8') as f:
            f.write(f"\r\n-------------\r\n{order}")

        print("\n\n*** Приятного аппетита! ***")


    def show_statistic(self):
        msg = f"""
            Всего продано пицц: {self.order.total_sales}
            Выручка: {self.order.revenue} руб.
            Прибыль: {self.order.profit} руб.  
        """
        print(msg)


