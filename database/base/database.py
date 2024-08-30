import asyncio
from typing import Annotated
from config import get_DB_URL
from datetime import datetime
from sqlalchemy import inspect, desc, func
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncAttrs, create_async_engine
from sqlalchemy.orm import Session, DeclarativeBase, declared_attr, Mapped, mapped_column

class Database(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    int_primary_key = Annotated[int, mapped_column(primary_key=True)]
    created_at = Annotated[datetime, mapped_column(server_default=func.now())]
    updated_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=datetime.now)]
    str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]
    str_null_true = Annotated[str, mapped_column(nullable=True)]

    def __init__(self):
        self.engine = create_async_engine(get_DB_URL())
        self.session: Session = async_sessionmaker(expire_on_commit=False, autocommit=False, autoflush=False, bind=self.engine)()
        async def create_tables():
            async with self.engine.begin() as conn:
                await conn.run_sync(self.metadata.create_all)
        asyncio.create_task(create_tables())

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    async def seed(self, instances):
        for index, instance in enumerate(instances):
            instance.id = index + 1
            await self.create_or_update(instance)

    async def create_or_update(self, instance):
        instance_properties = {attr.key: getattr(instance, attr.key) for attr in inspect(instance).mapper.column_attrs}
        instance_properties = {key: value for key, value in instance_properties.items() if value is not None}
        properties_for_update = instance_properties
        if 'id' in instance_properties:
            instance_properties = {key: value for key, value in instance_properties.items() if key == 'id'}
        filter_expressions = [getattr(type(instance), key) == value for key, value in instance_properties.items()]
        existing_record = self.session.query(type(instance)).filter(*filter_expressions).first()
        if existing_record:
            for attr, value in properties_for_update.items():
                setattr(existing_record, attr, value)
            setattr(existing_record, 'updated_at', datetime.utcnow())
        else:
            self.session.add(instance)
        self.session.commit()

    async def create(self, instance):
        self.session.add(instance)
        self.session.commit()

    async def get(self, instance):
        instance_properties = {attr.key: getattr(instance, attr.key) for attr in inspect(instance).mapper.column_attrs}
        instance_properties = {key: value for key, value in instance_properties.items() if value is not None}
        filter_expressions = [getattr(type(instance), key) == value for key, value in instance_properties.items()]
        return self.session.query(type(instance)).filter(*filter_expressions).order_by(desc(type(instance).id)).first()
    
    async def get_all(self, instance):
        return self.session.query(instance).order_by(desc(type(instance).id)).all()