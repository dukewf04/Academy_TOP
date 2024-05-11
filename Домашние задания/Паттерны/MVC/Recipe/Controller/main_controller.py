from Model.Recipe import Recipe

class RecipeController:
    """Рализация класса контроллер. Валидация данных, передача в модель."""
    def __init__(self):
        self.recipe = Recipe()

    def validate_data(self, data: dict):
        for el in data:
            if type(el) != str:
                print("Ошибка валидации данных")
                return

        self.recipe.add_recipe(data)


    def load_data(self):
        self.recipe.get_all_recipes()

    def finde_recipe(self, name):
        self.recipe.find_recipie(name)