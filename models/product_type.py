from models.base.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey

class ProductType(BaseModel):
    __tablename__ = 'product_types'
    type = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('product_groups.id'), index=True, nullable=False)

    def __init__(self, type=None, group_id=None):
        super().__init__()
        self.type = type
        self.group_id = group_id