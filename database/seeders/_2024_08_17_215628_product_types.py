import asyncio
from database.base.database import Database
from models import ProductType, ProductGroup
from database.seeders.base.base_seeder import BaseSeeder

class ProductTypes(BaseSeeder):
    revision: str = '_2024_08_17_215628'

    def __init__(self):
        async def seed():
            product_groups = await ProductGroup().get_all()
            await Database().seed([
                ProductType(
                    group_id=self.get_related(product_groups, group='Продукты').id, 
                    type='Овощи'
                ),
                ProductType(
                    group_id=self.get_related(product_groups, group='Продукты').id, 
                    type='Фрукты и ягоды'
                ),
                ProductType(
                    group_id=self.get_related(product_groups, group='Продукты').id, 
                    type='Молочные продукты'
                ),
                ProductType(
                    group_id=self.get_related(product_groups, group='Продукты').id, 
                    type='Мясные продукты'
                ),
                ProductType(
                    group_id=self.get_related(product_groups, group='Продукты').id, 
                    type='Замороженные продукты'
                ),
                ProductType(
                    group_id=self.get_related(product_groups, group='Продукты').id, 
                    type='Бакалея'
                ),
                ProductType(
                    group_id=self.get_related(product_groups, group='Продукты').id, 
                    type='Алкогольные напитки'
                ),
                ProductType(
                    group_id=self.get_related(product_groups, group='Бытовые товары').id, 
                    type='Личная гигиена'
                ),
                ProductType(
                    group_id=self.get_related(product_groups, group='Бытовые товары').id, 
                    type='Уборка'
                )
            ])
        asyncio.run(seed())