from Utils.Local import local

class FoodStore:
    """Модель для хранения информации по компонентам для создании хот-дога"""

    def __init__(self):
        # Задаем количество ингридиентов на складе
        self.food_components = dict.fromkeys(
            ["bun", "meat", "sausage", "bacon", "tomato", "chili", "avocado", "cabbage", "mayonnaise", "ketchup", "onion"],
            8
        )

    def get_components(self, components):
        """Метод, отвечающий за взятие ингридиентов со склада"""

        for el in components:
            self.food_components[el] -= 1

    def check_components(self, components: list):
        """Метод отвечающий за проверку, есть ли указанные компоненты на складе"""
        for el in components:
            if self.food_components[el] == 0:
                return False

        return True

    def check_how_much_components(self):
        """Метод для отслеживания, какие компоненты заканчиваются"""

        component_list = []
        for item in self.food_components.items():
            if item[1] <= 3:
                component_list.append(item)

        if len(component_list) == 0:
            return

        print("Список ингридиентов, которые заканчиваются:")
        result = ""
        for el in component_list:
            result += f"{local(el[0])} - {el[1]} шт\n"

        return result