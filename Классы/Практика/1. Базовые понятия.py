class Human:
    def __init__(self):
        self.fio = ''
        self.date = ''
        self.__tel = ''
        self.city = ''
        self.home = ''
        self.country = ''

    def getTel(self):
        return self.__tel

    def setTel(self, a):
        self.__tel = a

    def inputINFO(self):
        self.fio = input("Введите ФИО> ")
        self.date = input("Введите дату рождения> ")
        self.__tel = input("Введите конт. телефон> ")
        self.city = input("Введите город> ")
        self.home = input("Введите домашний адрес> ")
        self.country = input("Введите страну> ")

    def __str__(self):
        return (f"\nДанные человека:\n"
                f"{self.fio}\n"
                f"{self.city}\n"
                f"{self.home}\n"
                f"{self.__tel}\n"
                f"{self.date}\n"
                f"{self.country}")

human1 = Human()
human1.inputINFO()
print(human1)