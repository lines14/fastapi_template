import classutilities
from os import getenv
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base

class Database(classutilities.ClassPropertiesMixin):
    Base = declarative_base()

    def __init__(self):
        host = getenv('MYSQL_HOST')
        port = getenv('MYSQL_PORT')
        database = getenv('MYSQL_DATABASE')
        password = getenv('MYSQL_ROOT_PASSWORD')
        engine = create_engine(f'mysql+pymysql://root:{password}@{host}:{port}/{database}?charset=utf8mb4')
        self.session: Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
        self.Base.metadata.create_all(bind=engine)

    @classutilities.classproperty
    def base(self):
        return self.Base

    def seed(self, instances):
        for index, instance in enumerate(instances):
            instance.id = index + 1
            self.create_or_update(instance)

    def create_or_update(self, instance):
        instance_properties = {attr.key: getattr(instance, attr.key) for attr in inspect(instance).mapper.column_attrs}
        existing_record = self.session.query(type(instance)).order_by(type(instance).id).filter_by(id=instance.id).first()
        if existing_record:
            for attr, value in instance_properties.items():
                setattr(existing_record, attr, value)
        else:
            self.session.add(instance)
        self.session.commit()

    def create(self, instance):
        self.session.add(instance)
        self.session.commit()