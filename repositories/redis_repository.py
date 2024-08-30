from os import getenv
from typing import Dict
from config import Config
import redis.asyncio as redis

class RedisRepository:
    def __init__(self):
        pool = redis.ConnectionPool.from_url(Config().REDIS_URL)
        self.__client = redis.Redis(connection_pool=pool)

    async def set_user(self, user_login: str, user_token: str) -> None:
        await self.__client.setex(user_login, getenv('TTL'), user_token)

    async def get_user(self, user_login: str) -> Dict:
        return await self.__client.get(user_login)