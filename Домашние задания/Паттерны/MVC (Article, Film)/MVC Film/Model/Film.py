class Film:
    def __init__(self):
        self.name = ""
        self.genre = ""
        self.director = ""
        self.year = ""
        self.duratinon = ""
        self.studio = ""
        self.actors = ""

    def get_info(self):
        return f"""
            название фильма: {self.name}
            жанр: {self.genre}
            режисер: {self.director}
            год выпуска: {self.year}
            продолжительность: {self.duratinon}
            студия: {self.studio}
            actors: {self.actors}
        """
