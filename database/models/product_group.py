from sqlalchemy.sql import func
from database.base.database import Database
from sqlalchemy import Column, Integer, String, DateTime

class ProductGroup(Database.Base):
    __tablename__ = 'product_groups'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    group = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), nullable=False)

    def __init__(self, group=None):
        self.db = Database()
        self.group = group

    def get(self):
        return self.db.get(self)