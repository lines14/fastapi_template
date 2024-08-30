import asyncio
from database.base.database import Database
from database.models import ProductType, ProductGroup

class ProductTypes():
    revision: str = '_2024_08_17_215628'

    def __init__(self):
        async def seed():
            await Database().seed([
                ProductType(group_id=ProductGroup(group='Продукты').get().id, type='Овощи'),
                ProductType(group_id=ProductGroup(group='Продукты').get().id, type='Фрукты и ягоды'),
                ProductType(group_id=ProductGroup(group='Продукты').get().id, type='Молочные продукты'),
                ProductType(group_id=ProductGroup(group='Продукты').get().id, type='Мясные продукты'),
                ProductType(group_id=ProductGroup(group='Продукты').get().id, type='Замороженные продукты'),
                ProductType(group_id=ProductGroup(group='Продукты').get().id, type='Бакалея'),
                ProductType(group_id=ProductGroup(group='Продукты').get().id, type='Алкогольные напитки'),
                ProductType(group_id=ProductGroup(group='Бытовые товары').get().id, type='Личная гигиена'),
                ProductType(group_id=ProductGroup(group='Бытовые товары').get().id, type='Уборка')
            ])
        asyncio.create_task(seed())
