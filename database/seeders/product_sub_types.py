from database.database import Database
from models import ProductType, ProductSubType

class ProductSubTypes():
    def __init__(self):
        database = Database()
        database.seed([
            ProductSubType(type=database.get(ProductType(type='Продукты')).id, sub_type='Овощи'),
            ProductSubType(type=database.get(ProductType(type='Продукты')).id, sub_type='Фрукты'),
            ProductSubType(type=database.get(ProductType(type='Продукты')).id, sub_type='Молочные')
        ])