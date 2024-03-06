from modules.library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title: str, upc: str, subject: str, volume: str, issue: str):
        super().__init__(title, upc, subject)
        self.volume = volume
        self.issue = issue
