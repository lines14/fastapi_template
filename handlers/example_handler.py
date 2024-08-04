import traceback
from fastapi import Request
from utils.responses import Responses

class ExampleHandler:
    @staticmethod
    async def example(request: Request) -> str:
        try:
            data = await request.json()
            return await Responses.success("Success", data)
        except Exception as e:
            with open("log.txt", "a") as file:
                file.write(traceback.format_exc() + '\n')
            return await Responses.error(str(e))