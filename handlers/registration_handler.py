import traceback
from models import User
from utils.logger import Logger
from fastapi import Request, Response
from utils.data_utils import DataUtils
from utils.response_utils import ResponseUtils
from utils.cryptography_utils import CryptographyUtils

class RegistrationHandler:
    async def registration(self, request: Request) -> Response:
        try:
            request_data = await request.json()
            validated_data = User(**request_data)
            user = User(login=validated_data.login)
            if not await user.get():
                user.password=CryptographyUtils.hash_string(validated_data.password)
                await user.create()
                return await ResponseUtils.success(DataUtils.responses.registered)
            else:
                return await ResponseUtils.error(*DataUtils.responses.user_exists)
        except Exception as e:
            Logger.log(traceback.format_exc())
            return await ResponseUtils.error(str(e))