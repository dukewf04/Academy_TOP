from Model.Film import Film
from View.View import View


class Controller:
    def __init__(self, film: Film, view: View):
        self.film = film
        self.view = view

    def show_menu(self):
        self.view.display_menu(film=self.film)

    def show_film_info(self):
        self.view.display_article(film=self.film)
