import traceback
from fastapi import Request
from utils.logger import Logger
from utils.data_utils import DataUtils
from utils.response_utils import ResponseUtils
from services.currencies_service import CurrenciesService

class GreetingsHandler:
    async def greetings(self, request: Request) -> str:
        try:
            currencies_service = CurrenciesService()
            response = await currencies_service.get_rates()
            return await ResponseUtils.success(DataUtils.responses.info, response.text)
        except Exception as e:
            Logger.log(traceback.format_exc())
            return await ResponseUtils.error(str(e))
        
    # async def post(self, request: Request) -> str:
    #     try:
    #         data = await request.json()
    #         return await ResponseUtils.success("Success", data)
    #     except Exception as e:
    #         Logger.log(traceback.format_exc())
    #         return await ResponseUtils.error(str(e))