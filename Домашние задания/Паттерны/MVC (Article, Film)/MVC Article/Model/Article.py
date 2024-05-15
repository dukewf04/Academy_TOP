class Article:
    def __init__(self, title, author, symbol_count, publisher, description):
        self.title = title
        self.author = author
        self.symbol_count = symbol_count
        self.publisher = publisher
        self.description = description

    def get_info(self):
        return f"""
            название статьи: {self.title}
            автор статьи: {self.author}
            количество знаков: {self.symbol_count}
            название издания: {self.publisher}
            краткое описание: {self.description}
        """
