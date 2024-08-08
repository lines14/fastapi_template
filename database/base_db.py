from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class BaseDB:
    def __init__(self, host, port, database, password):
        self.Base = declarative_base()
        self.engine = create_engine(f'mysql+pymysql://root:{password}@{host}:{port}/{database}?charset=utf8mb4')
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base.metadata.create_all(bind=self.engine)
        print(self.Base.metadata.tables)