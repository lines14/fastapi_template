import redis
from os import getenv
from typing import Dict

class RedisRepository:
    def __init__(self):
        self.__client = redis.Redis(
            host=getenv('REDIS_HOST'),
            port=getenv('REDIS_PORT'),
            password=getenv('REDIS_PASSWORD')
        )

    def set_user(self, user_login: str, user_password: str) -> None:
        self.__client.set(user_login, user_password)

    def get_user(self, user_login: str) -> Dict:
        response = self.__client.get(user_login)
        return response.decode('utf-8')