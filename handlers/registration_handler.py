import traceback
from models import User
from fastapi import Response
from utils.logger import Logger
from utils.data_utils import DataUtils
from utils.response_utils import ResponseUtils
from utils.cryptography_utils import CryptographyUtils

class RegistrationHandler:
    async def registration(self, user: User) -> Response:
        try:
            existing_user = await User(login=user.login).get()
            if not existing_user:
                new_user = User(
                    login=user.login, 
                    password=CryptographyUtils.hash_string(user.password)
                )
                await new_user.create()
                return await ResponseUtils.success(DataUtils.responses.registered)
            else:
                return await ResponseUtils.error(*DataUtils.responses.user_exists)
        except Exception as e:
            Logger.log(traceback.format_exc())
            return await ResponseUtils.error(str(e))