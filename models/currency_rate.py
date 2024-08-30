from sqlalchemy.orm import Mapped
from database.base.database import Database

class CurrencyRate(Database):
    rate: Mapped[Database.float_not_nullable]
    currency_id: Mapped[Database.int_indexed_not_nullable]

    def __init__(self, rate=None, currency_id=None):
        self.rate = rate
        self.currency_id = currency_id