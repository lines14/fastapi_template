import asyncio
from models import ProductGroup
from database.base.database import Database

class ProductGroups():
    revision: str = '_2024_08_17_215610'

    def __init__(self):
        async def seed():
            async with Database() as database:
                await database.seed([
                    ProductGroup(group='Продукты'),
                    ProductGroup(group='Бытовые товары'),
                    ProductGroup(group='Электроника'),
                    ProductGroup(group='Одежда'),
                    ProductGroup(group='Услуги')
                ])
        asyncio.run(seed())