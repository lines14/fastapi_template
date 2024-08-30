import asyncio
from config import Config
from typing import Annotated
from datetime import datetime
from sqlalchemy import inspect, desc, func, select
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncAttrs, create_async_engine, AsyncSession

class Database(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    int_primary_key = Annotated[int, mapped_column(primary_key=True)]
    str_primary_key = Annotated[str, mapped_column(primary_key=True)]
    str_nullable_true = Annotated[str, mapped_column(nullable=True)]
    int_nullable_true = Annotated[int, mapped_column(nullable=True)]
    str_nullable_false = Annotated[str, mapped_column(nullable=False)]
    int_nullable_false = Annotated[int, mapped_column(nullable=False)]
    str_unique = Annotated[str, mapped_column(unique=True, nullable=False)]
    created_at = Annotated[datetime, mapped_column(server_default=func.now())]
    updated_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=datetime.now)]

    def __init__(self):
        engine = create_async_engine(Config().DB_URL)
        self.session: AsyncSession = async_sessionmaker(bind=engine, expire_on_commit=False, autocommit=False, autoflush=False)()
        async def create_tables():
            async with engine.begin() as conn:
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
        
        async with self.session.begin():
            stmt = select(type(instance)).filter(*filter_expressions)
            result = await self.session.execute(stmt)
            existing_record = result.scalar_one_or_none()

            if existing_record:
                for attr, value in properties_for_update.items():
                    setattr(existing_record, attr, value)
            else:
                self.session.add(instance)
            await self.session.commit()

    async def create(self, instance):
        async with self.session.begin():
            self.session.add(instance)
            await self.session.commit()

    async def get(self, instance):
        instance_properties = {attr.key: getattr(instance, attr.key) for attr in inspect(instance).mapper.column_attrs}
        instance_properties = {key: value for key, value in instance_properties.items() if value is not None}
        filter_expressions = [getattr(type(instance), key) == value for key, value in instance_properties.items()]
        
        async with self.session.begin():
            stmt = select(type(instance)).filter(*filter_expressions).order_by(desc(type(instance).id))
            result = await self.session.execute(stmt)
            return result.scalars().first()
    
    async def get_all(self, instance):
        async with self.session.begin():
            stmt = select(instance).order_by(desc(type(instance).id))
            result = await self.session.execute(stmt)
            return result.scalars().all()