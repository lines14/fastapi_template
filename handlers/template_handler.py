import traceback
from fastapi import Request
from utils.api_repsponse import send_error, send_success

class TemplateHandler:
    @staticmethod
    async def template(request: Request) -> str:
        try:
            data = await request.json()
            return send_success("Success", data)
        except Exception as e:
            with open("log.txt", "a") as file:
                file.write(traceback.format_exc() + '\n')
            return send_error(str(e))