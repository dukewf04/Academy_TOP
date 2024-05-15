from Model.Article import Article
from View.View import View
from Controller.Controller import Controller

if __name__ == "__main__":
    article = Article(
        "Мастер и Маргарита", "Булгаков", "10000", "Питер", "Фантастический роман"
    )
    view = View()
    controller = Controller(article, view)

    controller.show_article()
