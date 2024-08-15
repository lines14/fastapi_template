import traceback
from os import getenv
from models import User
from fastapi import Request
from utils.logger import Logger
from utils.JWT_utils import JWTUtils
from utils.data_utils import DataUtils
from database.database import Database
from utils.response_utils import ResponseUtils
from repositories.redis_repository import RedisRepository

database = Database()
redis_repository = RedisRepository()

class AuthHandler:
    async def auth(self, request: Request) -> str:
        try:
            request_data = await request.json()
            if (request_data['login'] == getenv('USER_LOGIN') 
            and request_data['password'] == getenv('USER_PASSWORD')):
                token = JWTUtils.generate_token(request_data['login'])
                redis_repository.set_user(request_data['login'], token)
                database.create(
                    User,
                    request_data['login'], 
                    JWTUtils.hash_token(token),
                    request.headers.get('host'),
                    request.headers.get('user-agent')
                )
                return await ResponseUtils.success("Success", token)
            else:
                return await ResponseUtils.error(*DataUtils.responses.invalidCredentials)
        except Exception as e:
            Logger.log(traceback.format_exc())
            return await ResponseUtils.error(str(e))