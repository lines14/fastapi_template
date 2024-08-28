import traceback
from os import getenv
from models import User
from fastapi import Request
from utils.logger import Logger
from utils.JWT_utils import JWTUtils
from utils.data_utils import DataUtils
from utils.response_utils import ResponseUtils
from repositories.redis_repository import RedisRepository

class AuthHandler:
    async def auth(self, request: Request) -> str:
        redis_repository = RedisRepository()
        try:
            request_data = await request.json()
            if (request_data['login'] == getenv('USER_LOGIN') 
            and request_data['password'] == getenv('USER_PASSWORD')):
                token = JWTUtils.generate_token(request_data['login'])
                redis_repository.set_user(request_data['login'], token)
                user = User(
                    login=request_data['login'], 
                    token=JWTUtils.hash_token(token),
                    host=request.headers.get('host'),
                    user_agent=request.headers.get('user-agent')
                )
                user.create()
                return await ResponseUtils.success("Success", token)
            else:
                return await ResponseUtils.error(*DataUtils.responses.invalidCredentials)
        except Exception as e:
            Logger.log(traceback.format_exc())
            return await ResponseUtils.error(str(e))