# class Products:
#     def __init__(self, name, price):
#         self.name = name
#         self.prise = price
#     def __repr__(self):
#         return f"Products Details: {self.name}, price: {self.prise}"
#
# pr = Products("Колбаса", "250")
#
# with open("file.txt", "w", encoding="utf-8") as f:
#     f.write(repr(pr))
#
# with open("file.txt", "r", encoding="utf-8") as f:
#     string2 = f.read()
#     print(string2)

import os
class CountryDict:
    def __init__(self):
        self.data = {}
        self.__filename = "Country.txt"

    def add_data(self, country: str, capital: str):
        self.data[country] = capital

    def remove_data(self, country):
        if country in self.data:
            del self.data[country]
        else:
            print("There is not that country!")

    def search_data(self, country):
        if country in self.data:
            return self.data[country]
        else:
            return "There is not that country!"

    def edit_data(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital
        else:
            return "There is not that country!"

    def save_data(self, filename):
        with open(filename, "w") as f:
            f.write(repr(self.data))

    def load_data(self, filename):
        if os.path.exists(self.__filename):
            with open(filename, "r") as f:
                self.data = eval(f.read())
        else:
            print("File does not exist!")

    def menu(self):
        print("*" * 11, "Welcome!")
        while True:
            print("Menu:\n1. Add data\n2. Remove data\n3. Search data\n4. Edit data\n"
                  "5. Save data\n6. Load data\n0. Exit")
            user_input = int(input("Your choise> "))
            if user_input == 1:
                country = input("Type country name> ")
                capital = input("Type country capital> ")
                self.add_data(country, capital)
            elif user_input == 2:
                self.remove_data(input("Type country, you want to be delited> "))
            elif user_input == 3:
                print(self.search_data(input("What country you search?> ")))
            elif user_input == 4:
                country = input("Type country name> ")
                if country in self.data:
                    self.edit_data(country, new_capital=input("Type new capital> "))
                else:
                    print("There is not that country")
            elif user_input == 5:
                self.save_data(self.__filename)
                print("Data saved")
            elif user_input == 6:
                self.load_data(self.__filename)
                print("Data loaded")
            elif user_input == 0:
                print("*"*11, "\n", "Goodbye!")
                break

cd = CountryDict()
cd.menu()
