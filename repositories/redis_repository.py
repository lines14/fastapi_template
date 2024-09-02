from os import getenv
from typing import Dict
from DTO import RedisDTO
from config import Config
import redis.asyncio as redis

class RedisRepository:
    def __init__(self):
        pool = redis.ConnectionPool.from_url(Config().REDIS_URL)
        self.__client = redis.Redis(connection_pool=pool)

    async def set_user(self, user_login: str, user_token: str) -> None:
        data = RedisDTO(
            name=user_login, 
            time=getenv('TOKEN_TTL'), 
            value=user_token
        )
        await self.__client.setex(
            data.name, 
            data.time, 
            data.value
        )

    async def get_user(self, user_login: str) -> Dict:
        return await self.__client.get(user_login)