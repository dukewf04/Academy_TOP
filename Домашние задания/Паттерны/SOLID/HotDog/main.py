from View.View import View
from Model.FoodStore import FoodStore
from Model.HotDog import HotDog


if __name__ == "__main__":
    # Инициализация объекта FoodStore. Там храним информацию по ингридиентам, остатке.
    food_store = FoodStore()

    # Инициализация объекта HotDog. В этом классе описаны все види хот-догов.
    hotdog = HotDog()

    # Инициализация объекта View. Класс представления, отображает пользовательское меню.
    view = View(hotdog, food_store)

    while True:
        view.main_menu()