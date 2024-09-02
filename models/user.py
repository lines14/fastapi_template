from sqlmodel import Field
from datetime import datetime
from DTO.base.rules import Login, Password
from models.base.base_model import BaseModel
from sqlalchemy import func, Column, DateTime

class User(BaseModel, table=True):
    __tablename__ = 'users'
    id: int = Field(primary_key=True, nullable=False)
    login: Login = Field(index=True, nullable=False)
    password: Password = Field(nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False, onupdate=func.now()))