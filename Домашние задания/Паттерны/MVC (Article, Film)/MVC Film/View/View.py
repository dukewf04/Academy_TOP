from Model.Film import Film


class View:
    def display_menu(self, film: Film):
        film.name = input("Введите название фильма> ")
        film.genre = input("Введите жанр фильма> ")
        film.director = input("Введите режисера фильма> ")
        film.year = input("Введите год выпуска фильма> ")
        film.duratinon = input("Введите продолжительность фильма> ")
        film.studio = input("Введите студию> ")
        film.actors = input("Введите актеров фильма (ФИО и роль)> ")

    def display_article(self, film: Film) -> None:
        print("\n*** Информация о фильме ***")
        print(film.get_info())
