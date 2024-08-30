import re
from config import Config
from datetime import datetime
from sqlalchemy import inspect, desc, select
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncAttrs, create_async_engine, AsyncSession

class Database(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    def __init__(self):
        self.engine = create_async_engine(Config().DB_URL_ASYNC)
        self.session: AsyncSession = async_sessionmaker(
            bind=self.engine, 
            expire_on_commit=False, 
            autocommit=False, 
            autoflush=False
        )

    async def init_tables(self):
        async with self.engine.begin() as connection:
            await connection.run_sync(self.metadata.create_all)

    async def __aenter__(self):
        self.session = self.session()
        await self.init_tables()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.engine.dispose()

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower() + 's'

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
            existing_record = ((await self.session.execute(select(type(instance))
                                                           .filter(*filter_expressions)
                                                           .order_by(desc(type(instance).id))))
                                                           .scalars()
                                                           .first())
            if existing_record:
                for attr, value in properties_for_update.items():
                    setattr(existing_record, attr, value)
                    setattr(existing_record, 'updated_at', datetime.utcnow())
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
            return ((await self.session.execute(select(type(instance))
                                                .filter(*filter_expressions)
                                                .order_by(desc(type(instance).id))))
                                                .scalars()
                                                .first())
    
    async def get_all(self, instance):
        async with self.session.begin():
            return (await self.session.execute(select(type(instance)))).scalars().all()