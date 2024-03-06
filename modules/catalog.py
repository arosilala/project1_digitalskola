from modules.book import Book
from modules.magazine import Magazine
from modules.library_item import LibraryItem
from modules.cd import Cd
from modules.dvd import Dvd

class Catalog():
    def __init__(self, catalog):
        self.catalog = catalog

    def search(self, input_search):
        list_result = []
        for catalog_item in self.catalog:
            for item in catalog_item:
                if input_search.lower() in item.title.lower():
                    item_type = self.get_item_type(item)
                    list_result.append(f'Title: {item.title}, {item_type}')
        return list_result

    def get_item_type(self, item):
        if isinstance(item, Magazine):
            return f'Volume: {item.volume}, Type: Magazine'
        elif isinstance(item, Book):
            return f'DDS Number: {item.dds_number}, Type: Book'
        elif isinstance(item, Cd):
            return f'Artist: {item.artist}, Type: Cd'
        elif isinstance(item, Dvd):
            return f'Genre: {item.genre}, Type: Dvd'
        else:
            return 'Unknown Type'
