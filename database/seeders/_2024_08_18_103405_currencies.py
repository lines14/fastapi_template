import asyncio
from database.models import Currency
from database.base.database import Database

class Currencies():
    revision: str = '_2024_08_18_103405'

    def __init__(self):
        async def seed():
            async with Database() as database:
                await database.seed([
                    Currency(currency='KZT'),
                    Currency(currency='RUB'),
                    Currency(currency='USD'),
                    Currency(currency='EUR')
                ])
        asyncio.create_task(seed())