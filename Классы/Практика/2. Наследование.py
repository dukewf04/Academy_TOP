class Auto:
    def __init__(self, namemodel, manufactorer, year, color, price, engincapacity):
        self.color = color
        self.year = year
        self.price = price
        self.manufactorer = manufactorer
        self.namemodel = namemodel
        self.engincapacity = engincapacity

    def inputAll(self):
        self.namemodel = input("Введите название модели: ")
        self.price = input("Введите цену: ")
        self.color = input("Введите цвет: ")
        self.year = input("Введите год выпуска: ")
        self.manufactorer = input("Введите название производителя: ")
        self.engincapacity = input("Введите объем двигателя: ")
        print(f"Операция выполнена!\n{'*' * 11}")
    def setInput(self, valueInput):
        if valueInput == 1:
            self.namemodel = input("Введите название модели: ")
        elif valueInput == 2:
            self.price = input("Введите цену: ")
        elif valueInput == 3:
            self.color = input("Введите цвет: ")
        elif valueInput == 4:
            self.year = input("Введите год выпуска: ")
        elif valueInput == 5:
            self.manufactorer = input("Введите название производителя: ")
        elif valueInput == 6:
            self.engincapacity = input("Введите объем двигателя: ")
        print(f"Операция выполнена!\n{'*'*11}")

    def __str__(self):
        return (f"Название модели: {self.namemodel}\n"
                f"Цена: {self.price}\n"
                f"Цвет: {self.color}\n"
                f"Год выпуска: {self.year}\n"
                f"Производитель: {self.manufactorer}\n"
                f"Объем двигателя: {self.engincapacity}\n"
                f"{'*'*11}\n")
    def menu(self):
        return ("1. Посмотреть информацию\n"
                "2. Дополнить информацию\n"
                "3. Изменить все\n"
                "0. Выход\n")
    def menuInput(self):
        print("1. Название модели\n"
                "2. Цена\n"
                "3. Цвет\n"
                "4. Год выпуска\n"
                "5. Производитель\n"
                "6. Объем двигателя")
        valueinput = int(input("Ваш выбор> "))
        self.setInput(valueinput)



auto = Auto(namemodel="Chevrole Aveo",
            manufactorer="Chevrole",
            year="2016",
            color="Green",
            price="1000000",
            engincapacity="1.4")
while True:
    print(auto.menu())
    value = int(input("Ваш выбор> "))
    if value == 1:
        print(auto)
    elif value == 2:
        auto.menuInput()
    elif value == 3:
        auto.inputAll()
    elif value == 0:
        break