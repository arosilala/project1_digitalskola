import json
from modules.book import Book
from modules.magazine import Magazine
from modules.cd import Cd
from modules.dvd import Dvd
from modules.catalog import Catalog

# Membuka file catalog.json
with open('files/catalog.json') as f:
    data_json = json.load(f)

# Mapping sumber objek ke kelas yang sesuai
source_to_class = {
    'book': Book,
    'magazine': Magazine,
    'cd': Cd,
    'dvd': Dvd
}

# Inisialisasi daftar untuk menyimpan instance objek yang sesuai dengan jenis item
catalog_items = {source: [] for source in source_to_class}

# Iterate melalui setiap item dalam data JSON dan membuat instance objek yang sesuai
for item in data_json:
    source = item['source']
    if source in source_to_class:
        catalog_items[source].append(
            source_to_class[source](**item)
        )

# Menyusun katalog dengan semua item yang sudah dibuat
catalog_all = [items for items in catalog_items.values()]

# Mencari item dengan input tertentu
input_search = 'test'
results = Catalog(catalog_all).search(input_search)

# Menampilkan hasil pencarian
for index, result in enumerate(results):
    print(f'result ke-{index+1} | {result}')
