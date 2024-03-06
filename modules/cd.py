from modules.library_item import LibraryItem

class Cd(LibraryItem):
    def __init__(self, title: str, upc: str, subject: str, artist: str):
        super().__init__(title, upc, subject)
        self.artist = artist
