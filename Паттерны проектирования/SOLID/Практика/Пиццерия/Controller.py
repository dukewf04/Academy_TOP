from View import View

class Controller:
    def __init__(self):
        self.view = View()

    def show_menu(self):
        self.view.show_menu()