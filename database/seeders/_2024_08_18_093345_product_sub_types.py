from database.database import Database
from models import ProductType, ProductSubType

class ProductSubTypes():
    revision: str = '_2024_08_18_093345'

    def __init__(self):
        database = Database()
        database.seed([
            ProductSubType(type=database.get(ProductType(type='Овощи')).id, sub_type='Огурцы'),
            ProductSubType(type=database.get(ProductType(type='Овощи')).id, sub_type='Помидоры'),
            ProductSubType(type=database.get(ProductType(type='Овощи')).id, sub_type='Помидоры черри'),
            ProductSubType(type=database.get(ProductType(type='Овощи')).id, sub_type='Салат'),
            ProductSubType(type=database.get(ProductType(type='Овощи')).id, sub_type='Перец'),
            ProductSubType(type=database.get(ProductType(type='Фрукты')).id, sub_type='Мандарины'),
            ProductSubType(type=database.get(ProductType(type='Фрукты')).id, sub_type='Апельсины'),
            ProductSubType(type=database.get(ProductType(type='Фрукты')).id, sub_type='Бананы'),
            ProductSubType(type=database.get(ProductType(type='Фрукты')).id, sub_type='Грейпфрут'),
            ProductSubType(type=database.get(ProductType(type='Фрукты')).id, sub_type='Лимон'),
            ProductSubType(type=database.get(ProductType(type='Фрукты')).id, sub_type='Слива'),
            ProductSubType(type=database.get(ProductType(type='Фрукты')).id, sub_type='Виноград'),
            ProductSubType(type=database.get(ProductType(type='Фрукты')).id, sub_type='Яблоки'),
            ProductSubType(type=database.get(ProductType(type='Фрукты')).id, sub_type='Нектарины'),
            ProductSubType(type=database.get(ProductType(type='Молочные продукты')).id, sub_type='Сыр'),
            ProductSubType(type=database.get(ProductType(type='Молочные продукты')).id, sub_type='Сырки'),
            ProductSubType(type=database.get(ProductType(type='Молочные продукты')).id, sub_type='Творог'),
            ProductSubType(type=database.get(ProductType(type='Молочные продукты')).id, sub_type='Йогурты'),
            ProductSubType(type=database.get(ProductType(type='Молочные продукты')).id, sub_type='Молоко'),
            ProductSubType(type=database.get(ProductType(type='Молочные продукты')).id, sub_type='Кисломолочные напитки'),
            ProductSubType(type=database.get(ProductType(type='Мясные продукты')).id, sub_type='Фарш'),
            ProductSubType(type=database.get(ProductType(type='Мясные продукты')).id, sub_type='Ветчина'),
            ProductSubType(type=database.get(ProductType(type='Мясные продукты')).id, sub_type='Колбаса'),
            ProductSubType(type=database.get(ProductType(type='Мясные продукты')).id, sub_type='Готовое мясо'),
            ProductSubType(type=database.get(ProductType(type='Мясные продукты')).id, sub_type='Сырое мясо'),
            ProductSubType(type=database.get(ProductType(type='Мясные продукты')).id, sub_type='Сосиски'),
            ProductSubType(type=database.get(ProductType(type='Мясные продукты')).id, sub_type='Сардельки'),
            ProductSubType(type=database.get(ProductType(type='Мясные продукты')).id, sub_type='Шпикачки')
        ])
