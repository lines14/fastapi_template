from sqlalchemy.orm import Mapped
from database.base.database import Database

class ProductSubType(Database):
    sub_type: Mapped[Database.str_not_nullable]
    type_id: Mapped[Database.int_indexed_not_nullable]

    def __init__(self, sub_type=None, type_id=None):
        self.sub_type = sub_type
        self.type_id = type_id