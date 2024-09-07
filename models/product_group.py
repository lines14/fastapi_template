from sqlalchemy import Column, String
from models.base.base_model import BaseModel

class ProductGroup(BaseModel):
    __tablename__ = 'product_groups'
    group = Column(String, nullable=False)

    def __init__(self, group=None):
        super().__init__()
        self.group = group