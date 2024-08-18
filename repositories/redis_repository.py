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

    def set_user(self, user_login: str, user_token: str) -> None:
        self.__client.setex(user_login, getenv('TTL'), user_token)

    def get_user(self, user_login: str) -> Dict:
        return self.__client.get(user_login)