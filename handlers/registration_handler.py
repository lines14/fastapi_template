import traceback
from fastapi import Request
from utils.logger import Logger
from database.models import User
from utils.data_utils import DataUtils
from utils.response_utils import ResponseUtils
from utils.cryptography_utils import CryptographyUtils

class RegistrationHandler:
    async def registration(self, request: Request) -> str:
        try:
            request_data = await request.json()
            if request_data['login'] and request_data['password']:
                user = User(login=request_data['login'])
                if not await user.get():
                    user.password=CryptographyUtils.hash_string(request_data['password'])
                    await user.create()
                    return await ResponseUtils.success(DataUtils.responses.registered)
                else:
                    return await ResponseUtils.error(*DataUtils.responses.user_exists)
            else:
                return await ResponseUtils.error(*DataUtils.responses.invalid_credentials)
        except Exception as e:
            Logger.log(traceback.format_exc())
            return await ResponseUtils.error(str(e))