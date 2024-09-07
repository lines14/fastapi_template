from sqlmodel import Field
from models.base.base_model import BaseModel

class User(BaseModel, table=True):
    __tablename__ = 'users'
    login: str = Field(index=True, nullable=False)
    password: str = Field(nullable=False)