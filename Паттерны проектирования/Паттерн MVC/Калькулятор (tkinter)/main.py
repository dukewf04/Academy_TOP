from view import MainApp
from tkinter import Tk

def main():
    root = Tk()  # Создание объекта окна
    root["bg"] = "#000"  #  Бэкграунд
    root.geometry("485x550+200+200")  # Задание геометрии формы
    root.resizable(False, False)  # Возможность маштабирования
    root.title("Калькулятор")
    app = MainApp(root)
    app.pack()
    root.mainloop()  #  Инициализация


if __name__ == "__main__":
    main()