from HotDog import HotDog
from FoodStore import FoodStore
from Order import Order
class Menu:
    """Класс, отвечающий за отображение пользовательского меню, уведомлений по наличию компонентов"""
    def __init__(self, food_store: FoodStore):
        self.food_store = food_store
        self.hotdog = HotDog()
        self.hotdog_list = [self.hotdog.classic, self.hotdog.sonora, self.hotdog.karolin]

    def show_menu(self):
        menu = "Выберите хот-дог:\n"
        for i, el in enumerate(self.hotdog_list):
            menu += f"[{i+1}] - {el['title']}. Ингридиенты: {el['definition']}. Цена: {el['cost']}\n"
        menu += "[0] - Оплатить заказ\n"
        print(menu)

        choice = int(input("> "))
        if choice in range(1, 4):
            if self.food_store.check_components(self.hotdog_list[choice-1]['components']):
                for el in self.hotdog_list[choice-1]['components']:
                    self.food_store.get_component(el)

            else:
                print("Недостаточно ингридиентов для этого хот-дога")

