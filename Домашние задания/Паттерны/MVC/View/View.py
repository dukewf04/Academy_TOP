from Controller.main_controller import ShoesController

shoes = ShoesController()

class MainView:
    """Реализация класса представление"""
    def __init__(self):
        pass

    def show(self):
        while True:
            print("Доступные команды:")
            print("1 - Сохранить данные об обуви в файл")
            print("2 - Загрузить данные об обуви")
            print("0 - Выход")
            choice = input("> ")
            if choice == '0':
                break
            if choice == '1':
                data = {
                    'gender_type': input("Введите тип обуви (мужская, женская)> "),
                    'type': input("Вид обуви (кроссовки, сапоги, сандалии, туфли и т.д.)> "),
                    'color': input("Введите цвет обуви> "),
                    'price': input("Введите цену обуви> "),
                    'manufactor': input("Введите производителя обуви> "),
                    'size': input("Введите размер обуви> "),
                }
                shoes.validate_data(data)
            elif choice == '2':
                shoes.load_data()