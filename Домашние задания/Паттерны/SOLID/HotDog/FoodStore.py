import json

class FoodStore:
    __file = 'food_store.json'
    """Модель для хранения информации по копонентам для создании хот-дога"""
    def __init__(self, bun, meat, sausage, bacon, cheese, onion, cucumber, tomato, chili, avocado, cabbage, jalapeno, mayonnaise, ketchup, mustard):
        # Задаем количество ингридиентов на складе
        self.__food_components = {
            "bun": bun,
            "meat": meat,
            "sausage": sausage,
            "bacon": bacon,
            "cheese": cheese,
            "onion": onion,
            "cucumber": cucumber,
            "tomato": tomato,
            "chili": chili,
            "avocado": avocado,
            "cabbage": cabbage,
            "jalapeno": jalapeno,
            "mayonnaise": mayonnaise,
            "ketchup": ketchup,
            "mustard": mustard
        }

        self.save_data()

    def save_data(self):
        with open(self.__file, 'w', encoding='utf-8') as f:
            json.dump(self.__food_components, f, indent=3, ensure_ascii=False)

    def get_component(self, component):
        """Метод, отвечающий за взятие ингридиентов со склада"""

        if self.__food_components[component] == 0:
            print(f"Компонент {component} закончился!")
            return False

        self.__food_components[component] -= 1
        self.save_data()

    def check_components(self, components: list):
        """Метод отвечающий за проверку, есть ли указанные компоненты на складе"""
        for el in components:
            if self.__food_components[el] == 0:
                return False

        return True