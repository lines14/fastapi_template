import traceback
from utils.logger import Logger
from models import User, Session
from utils.JWT_utils import JWTUtils
from fastapi import Request, Response
from utils.data_utils import DataUtils
from utils.response_utils import ResponseUtils
from utils.cryptography_utils import CryptographyUtils
from repositories.redis_repository import RedisRepository

class AuthHandler:
    async def auth(self, request: Request) -> Response:
        try:
            request_data = await request.json()
            validated_data = User(**request_data)
            user = await User(login=validated_data.login).get()
            if user and CryptographyUtils.verify_string(validated_data.password, user.password):
                token = JWTUtils.generate_token(validated_data.login)
                await RedisRepository().set_user(validated_data.login, token)
                session = Session(
                    login=validated_data.login, 
                    token=CryptographyUtils.hash_string(token),
                    host=request.headers.get('host'),
                    user_agent=request.headers.get('user-agent')
                )
                await session.create()
                return await ResponseUtils.success(DataUtils.responses.authorized, token)
            else:
                return await ResponseUtils.error(*DataUtils.responses.invalid_credentials)
        except Exception as e:
            Logger.log(traceback.format_exc())
            return await ResponseUtils.error(str(e))