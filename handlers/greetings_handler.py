import traceback
from fastapi import Request
from utils.logger import Logger
from utils.data_utils import DataUtils
from utils.response_utils import ResponseUtils

class GreetingsHandler:
    async def greetings(self, request: Request) -> str:
        try:
            return await ResponseUtils.success(DataUtils.responses.info)
        except Exception as e:
            Logger.log(traceback.format_exc())
            return await ResponseUtils.error(str(e))
        
    async def post(self, request: Request) -> str:
        try:
            data = await request.json()
            return await ResponseUtils.success("Success", data)
        except Exception as e:
            Logger.log(traceback.format_exc())
            return await ResponseUtils.error(str(e))