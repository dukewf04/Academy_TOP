import sys
from Utils.Local import local
from Model.HotDog import HotDog
from Model.FoodStore import FoodStore
from .Statistic import ViewStatistic
from .MenuHotdog import MenuHotdog

class View:
    """Класс, отвечающий за отображение пользовательского меню, уведомлений по наличию компонентов"""
    def __init__(self, hotdog: HotDog, food_store: FoodStore):
        self.hotdog = hotdog
        self.food_store = food_store

    def main_menu(self):
        # Сперва проверим каких компонентов осталось мало
        comp_list = self.food_store.check_how_much_components()
        print(comp_list) if comp_list else None

        menu = """
            Главное меню:
            1. Заказать хот-дог
            2. Статискика по проданным хотдогам
            3. Выход"""
        print(menu)
        choice = int(input("> "))
        if choice == 3:
            print("Всего хорошего!")
            sys.exit(0)

        if choice == 1:
            MenuHotdog.show_menu(self.hotdog, self.food_store)
        else:
            ViewStatistic.show_statistics(self.food_store)



