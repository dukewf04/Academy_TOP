from Model.HotDog import HotDog
from Utils.Local import locals, local
from Model.FoodStore import FoodStore
from Utils.Utils import counter_hotdog
from Model.Statistic import Statistic

class MenuHotdog:
    """Класс представлвения. Отображает пользовательское меню по заказу хотдогов"""

    order_list = []
    own_recipes = []
    dobavki_price = 0
    file_path = "order_history.txt"

    @staticmethod
    def show_menu(hotdog: HotDog, food_store: FoodStore):
        while True:
            msg = component_list = ""
            for i, el in enumerate(hotdog.hotdogs):
                component_list = ','.join(locals(el['components']))
                msg += f"{i+1}. {el['title']}. Ингридиенты: {component_list}. Цена: {el['price']} руб.\n"
            msg += f"4 - Создайте свой рецепт! (Цена: 300 руб)\n"
            msg += "0 - Перейти к оплате\n"
            print(msg)
            choice = int(input("> "))
            if choice == 0:
                break

            if choice == 4:
                MenuHotdog.own_recipes.append(input("Введите ваш рецепт хотдога> "))
                Statistic.buy_hotdog()
                continue

            # Проверяем достаточно ли компонентов на складе для создания хот-дога
            if food_store.check_components(hotdog.hotdogs[choice-1]['components']):
                MenuHotdog.order_list.append(hotdog.hotdogs[choice-1])
                Statistic.buy_hotdog()
                food_store.get_components(hotdog.hotdogs[choice-1]['components'])

                MenuHotdog.dobavka(hotdog)
            else:
                print("К сожалению ингридиенты для этого хотдога закончились( Попробуйте выбрать другой хот дог)\n")


        order = MenuHotdog.show_order(hotdog)
        oplata = input("Оплатите [1] - наличные, [2] по карте> ")

        with open(MenuHotdog.file_path, 'a', encoding='utf-8') as f:
            f.write(f"\r\n-------------\r\n{order}")

        print("\n\n*** Приятного аппетита! ***")
        MenuHotdog.order_list = []
        MenuHotdog.own_recipes = []
        MenuHotdog.dobavki_price = 0

    @staticmethod
    def show_order(hotdog: HotDog):
        """Отобразить текущий заказ"""

        order = ""
        total_cost = 0
        total_count = 0
        print("Ваш заказ:")
        for el in hotdog.hotdogs:
            count = counter_hotdog(MenuHotdog.order_list, el)
            if count > 0:
                order += f"{el['title']} - {count} шт\n"
                total_cost += el['price'] * count
                total_count += count

        for i, el in enumerate(MenuHotdog.own_recipes):
            order += f"- {el}\n"

        total_cost += MenuHotdog.dobavki_price + len(MenuHotdog.own_recipes) * 300
        total_count += len(MenuHotdog.own_recipes)
        # Производим расчет скидки
        if total_count >= 3:
            discount = Statistic.calculate_discount(total_count)
            order += f"Ваша скидка: {round(discount*100, 0)} %\n"
            total_cost -= total_cost * discount

        order += f"Итоговоя цена: {total_cost}"
        Statistic.calculate_profit(total_cost)
        print(order)

        return order

    @staticmethod
    def dobavka(hotdog: HotDog):
        """Метод отвечающий за вывод на экран информации по добавкам"""
        choice = int(input("Нужно ли добавить майнез, кетчуп для хотдога (1 - да, 0 - нет)?> "))
        if choice == 0:
            return

        for i, el in enumerate(hotdog.dobavki):
            print(f"[{i+1}] {local(el['title'])} - {el['price']} руб")

        choice = int(input("> "))
        MenuHotdog.dobavki_price += hotdog.dobavki[choice-1]['price']
