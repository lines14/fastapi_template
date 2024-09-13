from sqlmodel import Field
from models.base.base_model import BaseModel

class User(BaseModel, table=True):
    login: str = Field(index=True, nullable=False)
    hashed_password: str = Field(nullable=False)