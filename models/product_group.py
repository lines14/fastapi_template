from sqlmodel import Field
from models.base.base_model import BaseModel

class ProductGroup(BaseModel, table=True):
    group: str = Field(nullable=False)