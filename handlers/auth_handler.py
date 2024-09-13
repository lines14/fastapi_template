import traceback
from DTO import UserDTO
from utils.logger import Logger
from models import User, Session
from utils.JWT_utils import JWTUtils
from fastapi import Request, Response
from utils.data_utils import DataUtils
from utils.response_utils import ResponseUtils
from utils.cryptography_utils import CryptographyUtils
from repositories.redis_repository import RedisRepository

class AuthHandler:
    async def auth(self, request: Request, user: UserDTO) -> Response:
        try:
            existing_user = await User(login=user.login).get()
            if existing_user and CryptographyUtils.verify_string(user.password, existing_user.hashed_password):
                token = JWTUtils.generate_token(user.login)
                await RedisRepository().set_user(user.login, token)
                session = Session(
                    login=user.login, 
                    token=CryptographyUtils.hash_string(token),
                    host=request.headers.get('host'),
                    user_agent=request.headers.get('user-agent')
                )
                await session.create()
                return await ResponseUtils.success(DataUtils.responses.authorized_message, token)
            else:
                return await ResponseUtils.error(*DataUtils.responses.invalid_credentials_error)
        except Exception as e:
            Logger.log(traceback.format_exc())
            return await ResponseUtils.error(str(e))