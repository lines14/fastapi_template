from database.database import Database
from models import ProductType, ProductGroup

class ProductTypes():
    revision: str = '_2024_08_17_215628'

    def __init__(self):
        database = Database()
        database.seed([
            ProductType(group=database.get(ProductGroup(group='Продукты')).id, type='Овощи'),
            ProductType(group=database.get(ProductGroup(group='Продукты')).id, type='Фрукты'),
            ProductType(group=database.get(ProductGroup(group='Продукты')).id, type='Молочные продукты'),
            ProductType(group=database.get(ProductGroup(group='Продукты')).id, type='Мясные продукты'),
            ProductType(group=database.get(ProductGroup(group='Продукты')).id, type='Бакалея')
        ])
