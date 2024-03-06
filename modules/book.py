from modules.library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title: str, upc: str, subject: str, issbn: str, authors: str, dds_number: str):
        super().__init__(title, upc, subject)
        self.issbn = issbn
        self.authors = authors
        self.dds_number = dds_number

book1 = Book(
    title='Test book',
    upc='',
    subject='this is subject',
    issbn='',
    authors='',
    dds_number=''
)

print(book1.title)