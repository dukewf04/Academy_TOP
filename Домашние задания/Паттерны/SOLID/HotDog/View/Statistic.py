from Model.FoodStore import FoodStore
from Utils.Local import local
from Model.Statistic import Statistic

class ViewStatistic:
    """Класс представление. Отображает информацию по проданным хотдогам, выручке."""

    @staticmethod
    def show_statistics(food_store: FoodStore):
        remaining_products = [f"{local(key)} - {food_store.food_components[key]}" for key in food_store.food_components]
        msg = f"""
            Количество проданных хотдогов: {Statistic.total_count}.
            Выручка: {Statistic.revenue} руб.
            Прибыль: {Statistic.profit} руб.            
            Информация по оставшимся компонентам для приготавления хотдогов:
            {remaining_products}
        """

        return print(msg)

