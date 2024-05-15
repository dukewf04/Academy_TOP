from Model.Article import Article
from View.View import View


class Controller:
    def __init__(self, article: Article, view: View):
        self.article = article
        self.view = view

    def show_article(self):
        self.view.display_article(article=self.article)
