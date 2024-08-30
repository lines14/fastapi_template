from datetime import datetime
from sqlmodel import SQLModel, Field
from database.base.database import Database
from sqlalchemy import func, Column, func, DateTime

class ProductGroup(SQLModel):
    id: int = Field(primary_key=True, nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False, onupdate=datetime.now))
    group: str = Field(nullable=False)

    def __init__(self, group=None):
        self.group = group

    async def get(self):
        async with Database() as database:
            return await database.get(self)