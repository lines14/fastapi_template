import traceback
from fastapi import Request
from utils.logger import Logger
from utils.JWT_utils import JWTUtils
from utils.data_utils import DataUtils
from database.models import User, Session
from utils.response_utils import ResponseUtils
from utils.cryptography_utils import CryptographyUtils
from repositories.redis_repository import RedisRepository

class AuthHandler:
    async def auth(self, request: Request) -> str:
        redis_repository = RedisRepository()
        try:
            request_data = await request.json()
            if request_data['login'] and request_data['password']:
                user = await User(login=request_data['login']).get()
                if user and CryptographyUtils.verify_string(request_data['password'], user.password):
                    token = JWTUtils.generate_token(request_data['login'])
                    redis_repository.set_user(request_data['login'], token)
                    session = Session(
                        login=request_data['login'], 
                        token=CryptographyUtils.hash_string(token),
                        host=request.headers.get('host'),
                        user_agent=request.headers.get('user-agent')
                    )
                    await session.create()
                    return await ResponseUtils.success(DataUtils.responses.authorized, token)
                else:
                    return await ResponseUtils.error(*DataUtils.responses.invalid_credentials)
            else:
                return await ResponseUtils.error(*DataUtils.responses.invalid_credentials)
        except Exception as e:
            Logger.log(traceback.format_exc())
            return await ResponseUtils.error(str(e))