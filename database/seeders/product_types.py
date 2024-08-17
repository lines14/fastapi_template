from models import ProductType
from database.database import Database

class ProductTypes():
    def __init__(self):
        database = Database()
        database.seed([
            ProductType(type='Продукты'),
            ProductType(type='Бытовые товары'),
            ProductType(type='Электроника')
        ])