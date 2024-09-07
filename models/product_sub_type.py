from models.base.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey

class ProductSubType(BaseModel):
    __tablename__ = 'product_sub_types'
    sub_type = Column(String, nullable=False)
    type_id = Column(Integer, ForeignKey('product_types.id'), index=True, nullable=False)

    def __init__(self, sub_type=None, type_id=None):
        super().__init__()
        self.sub_type = sub_type
        self.type_id = type_id