from Pizza import Pizza

class View:
    def __init__(self):
        self.pizza = Pizza()

    def show_menu(self):
        print("Выберите пиццу:")
        for i, el in enumerate(self.pizza.pizza_list):
            print(f"[{i+1}] {el['name']}, цена - {el['price']}")
        pizza = int(input("> "))

        print("\nКакой топпинг добавить:")
        for i, el in enumerate(self.pizza.topping_list):
            print(f"[{i+1}] {el}")
        topping = int(input("> "))

        print("\nВаш заказ:")
        print(f"Пицца {self.pizza.pizza_list[pizza-1]['name']}, топпинг: {self.pizza.topping_list[topping-1]}. Стоимость {self.pizza.pizza_list[pizza-1]['price']}")
