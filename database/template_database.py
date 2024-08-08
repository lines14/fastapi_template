from os import getenv
from database.models import User
from sqlalchemy.orm import Session
from database.base_db import BaseDB

class TemplateDatabase(BaseDB):
    def __init__(self):
        HOST = getenv('MYSQL_HOST')
        PORT = getenv('MYSQL_PORT')
        DATABASE = getenv('MYSQL_DATABASE')
        PASSWORD = getenv('MYSQL_ROOT_PASSWORD')
        super().__init__(HOST, PORT, DATABASE, PASSWORD)
        self.session: Session = self.SessionLocal()

    def createUser(self, login):
        new_user = User(login=login)
        self.session.add(new_user)
        self.session.commit()