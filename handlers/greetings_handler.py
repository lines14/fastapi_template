import traceback
from utils.logger import Logger
from fastapi import Request, Response
from utils.data_utils import DataUtils
from utils.response_utils import ResponseUtils

class GreetingsHandler:
    async def greetings(self, request: Request) -> Response:
        try:
            return await ResponseUtils.success(DataUtils.responses.info)
        except Exception as e:
            Logger.log(traceback.format_exc())
            return await ResponseUtils.error(str(e))