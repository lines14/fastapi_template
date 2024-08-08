from os import getenv
from database.models import User
from sqlalchemy.orm import Session
from database.base.base_db import BaseDB

class TemplateDatabase(BaseDB):
    def __init__(self):
        super().__init__(
            getenv('MYSQL_HOST'), 
            getenv('MYSQL_PORT'), 
            getenv('MYSQL_DATABASE'), 
            getenv('MYSQL_ROOT_PASSWORD')
        )
        self.session: Session = self.SessionLocal()

    def create_user(self, login, token):
        new_user = User(login=login, token=token)
        self.session.add(new_user)
        self.session.commit()