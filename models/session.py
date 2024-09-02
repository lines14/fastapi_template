from sqlmodel import Field
from datetime import datetime
from DTO.base.rules import Login
from models.base.base_model import BaseModel
from sqlalchemy import func, Column, func, DateTime

class Session(BaseModel, table=True):
    __tablename__ = 'sessions'
    id: int = Field(primary_key=True, nullable=False)
    login: Login = Field(index=True, nullable=False)
    host: str = Field(nullable=False)
    user_agent: str = Field(nullable=False)
    token: str = Field(nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False, onupdate=func.now()))