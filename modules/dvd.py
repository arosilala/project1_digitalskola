class Dvd:
    def __init__(self, title: str, subject: str, upc: str, genre: str, actors: list = None, directors: list = None):
        self.title = title
        self.subject = subject
        self.upc = upc
        self.genre = genre
        self.actors = actors
        self.directors = directors
