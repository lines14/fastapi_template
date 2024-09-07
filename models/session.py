from sqlmodel import Field
from models.base.base_model import BaseModel

class Session(BaseModel, table=True):
    login: str = Field(index=True, nullable=False)
    host: str = Field(nullable=False)
    user_agent: str = Field(nullable=False)
    token: str = Field(nullable=False)