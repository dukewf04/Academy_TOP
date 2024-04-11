import os

# Task 1 (Country - Capital)
# class CountryDict:
#     def __init__(self):
#         self.data = {}
#         self.__filename = "Country.txt"
#
#     def add_data(self, country: str, capital: str):
#         self.data[country] = capital
#
#     def remove_data(self, country):
#         if country in self.data:
#             del self.data[country]
#         else:
#             print("There is not that country!")
#
#     def search_data(self, country):
#         if country in self.data:
#             return self.data[country]
#         else:
#             return "There is not that country!"
#
#     def edit_data(self, country, new_capital):
#         if country in self.data:
#             self.data[country] = new_capital
#         else:
#             return "There is not that country!"
#
#     def save_data(self, filename):
#         with open(filename, "w") as f:
#             f.write(repr(self.data))
#
#     def load_data(self, filename):
#         if os.path.exists(self.__filename):
#             with open(filename, "r") as f:
#                 self.data = eval(f.read())
#             print("Data loaded!")
#         else:
#             print("File does not exist!")
#
#     def menu(self):
#         print("*" * 11, "Welcome!")
#         while True:
#             print("Menu:\n1. Add data\n2. Remove data\n3. Search data\n4. Edit data\n"
#                   "5. Save data\n6. Load data\n0. Exit")
#             user_input = int(input("Your choise> "))
#             if user_input == 1:
#                 country = input("Type country name> ")
#                 capital = input("Type country capital> ")
#                 self.add_data(country, capital)
#             elif user_input == 2:
#                 self.remove_data(input("Type country, you want to be delited> "))
#             elif user_input == 3:
#                 print(self.search_data(input("What country you search?> ")))
#             elif user_input == 4:
#                 country = input("Type country name> ")
#                 if country in self.data:
#                     self.edit_data(country, new_capital=input("Type new capital> "))
#                 else:
#                     print("There is not that country")
#             elif user_input == 5:
#                 self.save_data(self.__filename)
#                 print("Data saved")
#             elif user_input == 6:
#                 self.load_data(self.__filename)
#             elif user_input == 0:
#                 print("*"*11, "\n", "Goodbye!")
#                 break
#
# cd = CountryDict()
# cd.menu()


# Task 2 (Музыкальные группы - альбомы)
# class MusicDict:
#     def __init__(self):
#         self.data = {}
#         self.__filename = "MusicDict.txt"
#
#     def add_data(self, artist: str, album: str):
#         self.data[artist] = album
#
#     def remove_data(self, artist):
#         if artist in self.data:
#             del self.data[artist]
#         else:
#             print("There is not that artist!")
#
#     def search_data(self, artist):
#         if artist in self.data:
#             return self.data[artist]
#         else:
#             return "There is not that artist!"
#
#     def edit_data(self, artist, new_album):
#         if artist in self.data:
#             self.data[artist] = new_album
#         else:
#             return "There is not that artist!"
#
#     def save_data(self, filename):
#         with open(filename, "w") as f:
#             f.write(repr(self.data))
#
#     def load_data(self, filename):
#         if os.path.exists(self.__filename):
#             with open(filename, "r") as f:
#                 self.data = eval(f.read())
#             print("Data loaded!")
#         else:
#             print("File does not exist!")
#
#     def menu(self):
#         print("*" * 11, "Welcome!")
#         while True:
#             print("Menu:\n1. Add data\n2. Remove data\n3. Search data\n4. Edit data\n"
#                   "5. Save data\n6. Load data\n0. Exit")
#             user_input = int(input("Your choise> "))
#             if user_input == 1:
#                 artist = input("Type artist name> ")
#                 capital = input("Type artist album> ")
#                 self.add_data(artist, capital)
#             elif user_input == 2:
#                 self.remove_data(input("Type artist, you want to be delited> "))
#             elif user_input == 3:
#                 print(self.search_data(input("What artist you search?> ")))
#             elif user_input == 4:
#                 artist = input("Type artist name> ")
#                 if artist in self.data:
#                     self.edit_data(artist, new_album=input("Type new album> "))
#                 else:
#                     print("There is not that artist")
#             elif user_input == 5:
#                 self.save_data(self.__filename)
#                 print("Data saved")
#             elif user_input == 6:
#                 self.load_data(self.__filename)
#             elif user_input == 0:
#                 print("*"*11, "\n", "Goodbye!")
#                 break
#
# md = MusicDict()
# md.menu()
