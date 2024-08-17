from models import ProductGroup
from database.database import Database

class ProductGroups():
    revision: str = '_2024_08_17_215610'

    def __init__(self):
        database = Database()
        database.seed([
            ProductGroup(group='Продукты'),
            ProductGroup(group='Бытовые товары'),
            ProductGroup(group='Электроника')
        ])
