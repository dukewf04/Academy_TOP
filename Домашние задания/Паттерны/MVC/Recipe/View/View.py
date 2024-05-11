from Controller.main_controller import RecipeController


class MainView:
    """Реализация класса представление"""

    def __init__(self):
        self.recipe_controller = RecipeController()

    def show(self):
        while True:
            print("Доступные команды:")
            print("1 - Добавить рецепт")
            print("2 - Вывести список рецептов на экран")
            print("3 - Найти рецепт")
            print("0 - Выход")
            choice = input("> ")
            if choice == '0':
                break
            if choice == '1':
                data = {
                    'name': input("Введите название рецепта> "),
                    'author': input("Автор рецепта> "),
                    'type': input("Тип рецепта> "),
                    'title': input("Текстовое описание рецепта> "),
                    'link': input("Ссылка на видео с рецептом> "),
                    'ingredients_list': input("Список ингридиентов> "),
                    'kitchen_name': input("Название кухни> "),
                }
                self.recipe_controller.validate_data(data)
            elif choice == '2':
                self.recipe_controller.load_data()
            elif choice == '3':
                name = input("Введите название рецепта> ")
                self.recipe_controller.finde_recipe(name)