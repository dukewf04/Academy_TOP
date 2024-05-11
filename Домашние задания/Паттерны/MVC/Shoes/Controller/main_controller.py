from Model.Shoes import Shoes

class ShoesController:
    """Рализация класса контроллер. Выполянет валидацию данных.
    Затем передаем корерктные данные в модель."""
    def __init__(self):
        self.shoes = Shoes()

    def validate_data(self, data: dict):
        if set(data.keys()) == set(self.shoes.SHOES_STRUCTURE.keys()) and data['gender_type'].lower() in ('мужская', 'женская'):
            self.shoes.save_data(data)
        else:
            print("Ошибка валидации данных!")


    def load_data(self):
        self.shoes.load_data()