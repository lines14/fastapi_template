from os import getenv
from database.models import User
from sqlalchemy.orm import Session
from database.base.base_db import BaseDB

class TemplateDatabase(BaseDB):
    def __init__(self):
        HOST = getenv('MYSQL_HOST')
        PORT = getenv('MYSQL_PORT')
        USER = getenv('MYSQL_USER')
        PASSWORD = getenv('MYSQL_PASSWORD')
        DATABASE = getenv('MYSQL_DATABASE')
        super().__init__(HOST, PORT, DATABASE, USER, PASSWORD)
        self.session: Session = self.SessionLocal()

    def create_user(self, login, token):
        new_user = User(login=login, token=token)
        self.session.add(new_user)
        self.session.commit()