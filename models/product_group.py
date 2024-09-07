from sqlmodel import Field
from models.base.base_model import BaseModel

class ProductGroup(BaseModel, table=True):
    __tablename__ = 'product_groups'
    group: str = Field(nullable=False)