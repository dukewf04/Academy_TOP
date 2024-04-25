# Task 1 (Паттерн Command)
# from sys import stdout as console
#
# # Обработка команды exit
# class SessionClosed(Exception):
#     def __init__(self, value):
#         self.value = value
#
# # Интерфейс команды
# class Command:
#     def execute(self):
#         raise NotImplementedError()
#     def cancel(self):
#         raise NotImplementedError()
#     def name(self):
#         raise NotImplementedError()
#
# # Команда rm
# class RmCommand(Command):
#     def execute(self):
#         console.write("you are executed \"rm \" command \n")
#     def canesl(self):
#         console.write("you are executed \"rm \" command \n")
#     def name(self):
#         return "rm"
#
# # Команда uptime
# class UpTimeCommand(Command):
#     def execute(self):
#         console.write("you are executed \"rm \" command \n")
#     def canesl(self):
#         console.write("you are executed \"rm \" command \n")
#     def name(self):
#         return "uptime"
#
# # Команда undo
# class UndoCommand(Command):
#     def execute(self):
#         try:
#             cmd = HISTORY.pop()
#             TRASH.append(cmd)
#             console.write("Undo command \" [0] \" \n".format(cmd.name()))
#             cmd.cancel()
#         except IndexError:
#             console.write("ERROR: HISTORY is empty \n")
#     def name(self):
#         return "undo"
#
# # Команда redo
# class RedoCommand(Command):
#     def execute(self):
#         try:
#             cmd = HISTORY.pop()
#             TRASH.append(cmd)
#             console.write("Redo command \" [0] \" \n".format(cmd.name()))
#             cmd.cancel()
#         except IndexError:
#             console.write("ERROR: HISTORY is empty \n")
#     def name(self):
#         return "undo"
#
# # Команда History
# class HistoryCommand(Command):
#     def execute(self):
#         i = 0
#         for cmd in HISTORY:
#             console.write("[0]: [1]\n".format(i, cmd.name()))
#             i += 1
#     def name(self):
#         print("History")
#
# # Команда exit
# class ExitCommand(Command):
#     def execute(self):
#         raise SessionClosed("Goodbye!")
#
#     def name(self):
#         return "exit"
#
# COMMANDS = {"rm": RmCommand(), "uptime": UpTimeCommand(), "undo": UndoCommand(), "redo": RedoCommand(), "history": HistoryCommand(), "exit": ExitCommand()}
# HISTORY = list()
# TRASH = list()
#
# def main():
#     try:
#         while True:
#             console.flush()
#             console.write("pysh >> ")
#             cmd = input()
#             try:
#                 command = COMMANDS[cmd]
#                 command.execute()
#                 if not isinstance(command, UndoCommand) and not isinstance(command, RedoCommand) and not isinstance(command, HistoryCommand):
#                     TRASH = list()
#                     HISTORY.append(command)
#             except KeyError:
#                 console.write("ERROR: HISTORY is empty \n")
#     except SessionClosed as e:
#         console.write(e.value)
#
# if __name__ == "__main__":
#     main()


# Task 2 (паттерн Proxy)
# import time
# import random
#
# class NumberSet:
#     """Класс для получения чисел из файла."""
#     def get_numbers(self):
#         with open("numbers.txt", "r", encoding="utf-8") as file:
#             data = file.read()
#             data = list(data.strip().split())
#             data = list(map(int, data))
#             return data
#
#     def refresh_numbers(self):
#         with open("numbers.txt", "w", encoding="utf-8") as file:
#             numbers_list = [random.randint(1, 99) for _ in range(10)]
#             numbers_list = list(map(str, numbers_list))
#             file.write(" ".join(numbers_list))
#
#
# # Прокси-класс для логгирования
# class NumberSetProxy:
#     def __init__(self):
#         self.number_set = NumberSet()
#
#     def get_numbers(self):
#         numbers = self.number_set.get_numbers()
#
#         # Логгирование при каждом доступе к данным
#         with open("log.txt", "a", encoding="utf-8") as file:
#             file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} Получен доступ к файлу\n")
#
#         return numbers
#
# if __name__ == "__main__":
#     number_set_proxy = NumberSetProxy()
#     for _ in range(5):
#         time.sleep(2)
#         number_set_proxy.number_set.refresh_numbers()
#         numbers = number_set_proxy.get_numbers()
#         print("Sum:", sum(numbers))
#         print("Max:", max(numbers))
#         print("Min:", min(numbers), "\n")



# Task 3 (Библиотека)
# import logging
#
# class Book:
#     def __init__(self, title, author, genre):
#         self.title = title
#         self.author = author
#         self.genre = genre
#
#     def __str__(self):
#         return f"{self.title} by {self.author} ({self.genre})"
#
# class Librarian:
#     def __init__(self, name):
#         self.name = name
#
# class Reader:
#     def __init__(self, name):
#         self.name = name
#
# class LibraryApp:
#     _instance = None
#
#     @classmethod
#     def getInstance(cls):
#         if not cls._instance:
#             cls.__instance = LibraryApp()
#         return cls._instance
#
#     def __init__(self):
#         self.bookshelf = []
#
#     def add_book(self, book):
#         self.bookshelf.append(book)
#         logging.info(f"Добавлена книга: {book}")
#
#     def remove_book(self, title):
#         for book in self.bookshelf:
#             if book.title == title:
#                 self.bookshelf.remove(book)
#                 logging.info(f"Книга удалена: {book}")
#                 break
#         else:
#             logging.warning(f"Книга с названием {title} не найдена")
#
#     def search_books_by_author(self, author):
#         found_books = []
#         for book in self.bookshelf:
#             if book.author == author:
#                 found_books.append(book)
#         if found_books:
#             return found_books
#         else:
#             return None
#
#     def save_to_file(self, filename):
#         with open(filename, 'w', encoding='utf-8') as file:
#             for book in self.bookshelf:
#                 file.write(f"{book.title},{book.author},{book.genre}\n")
#         logging.info("Данные сохранены в файл")
#
#     def load_from_file(self, filename):
#         with open(filename, 'r', encoding='utf-8') as file:
#             for line in file:
#                 title, author, genre = line.strip().split(',')
#                 self.add_book(Book(title, author, genre))
#         logging.info("Данные загружены из файла")
#
# if __name__ == "__main__":
#     logging.basicConfig(filename='library.log', level=logging.INFO, format='%(asctime)s - %(message)s', encoding='utf-8')
#
#     app = LibraryApp()
#     app.getInstance()
#
#     book1 = Book("Мастер и Маргарита", "Булгаков", "Фантастика")
#     book2 = Book("Анна Каренина", "Лев Толстой", "Роман")
#
#     app.add_book(book1)
#     app.add_book(book2)
#
#     app.save_to_file("library_data.txt")
#
#     app.remove_book("Мастер и Маргарита")
#
#     app.load_from_file("library_data.txt")
#
#     found_books = app.search_books_by_author("Лев Толстой")
#     if found_books:
#         for book in found_books:
#             print(book)
#     else:
#         print("Ни одной книги не найдено по автору")