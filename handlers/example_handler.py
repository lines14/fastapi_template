import traceback
from fastapi import Request
from utils.response_utils import ResponseUtils

class ExampleHandler:
    async def example(self, request: Request) -> str:
        try:
            data = await request.json()
            return await ResponseUtils.success("Success", data)
        except Exception as e:
            with open("log.txt", "a") as file:
                file.write(traceback.format_exc() + '\n')
            return await ResponseUtils.error(str(e))