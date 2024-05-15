from Model.Article import Article


class View:
    def display_article(self, article: Article) -> None:
        print(article.get_info())
