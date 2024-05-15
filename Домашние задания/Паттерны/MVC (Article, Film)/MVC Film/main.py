from Model.Film import Film
from View.View import View
from Controller.Controller import Controller

if __name__ == "__main__":
    film = Film()
    view = View()
    controller = Controller(film, view)

    controller.show_menu()
    controller.show_film_info()
