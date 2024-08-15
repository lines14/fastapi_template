import classutilities
from os import getenv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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

    def create(self, model, *args):
        self.session.add(model(*args))
        self.session.commit()