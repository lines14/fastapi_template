import redis
from os import getenv
from typing import Dict

class RedisRepository:
    def __init__(self):
        self._client = redis.Redis(
            host=getenv('REDIS_HOST'),
            port=getenv('REDIS_PORT'),
            password=getenv('REDIS_PASSWORD')
        )

    def get_user(self ,user_id: str) -> Dict:
        response = self._client.get('database_users' + user_id)
        return response.decode('utf-8')