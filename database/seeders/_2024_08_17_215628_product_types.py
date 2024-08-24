from database.database import Database
from models import ProductType, ProductGroup

class ProductTypes():
    revision: str = '_2024_08_17_215628'

    def __init__(self):
        database = Database()
        database.seed([
            ProductType(group_id=database.get(ProductGroup(group='Продукты')).id, type='Овощи'),
            ProductType(group_id=database.get(ProductGroup(group='Продукты')).id, type='Фрукты и ягоды'),
            ProductType(group_id=database.get(ProductGroup(group='Продукты')).id, type='Молочные продукты'),
            ProductType(group_id=database.get(ProductGroup(group='Продукты')).id, type='Мясные продукты'),
            ProductType(group_id=database.get(ProductGroup(group='Продукты')).id, type='Замороженные продукты'),
            ProductType(group_id=database.get(ProductGroup(group='Продукты')).id, type='Бакалея'),
            ProductType(group_id=database.get(ProductGroup(group='Продукты')).id, type='Алкогольные напитки'),
            ProductType(group_id=database.get(ProductGroup(group='Бытовые товары')).id, type='Личная гигиена'),
            ProductType(group_id=database.get(ProductGroup(group='Бытовые товары')).id, type='Уборка')
        ])
