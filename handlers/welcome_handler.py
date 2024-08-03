from sys import version
from fastapi import Request, __version__
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

class WelcomeHandler:
    @staticmethod
    async def welcome(request: Request) -> str:
        data = {
            'request': request,
            'pyVersion': version,
            'fastapiVersion': __version__
        }

        return templates.TemplateResponse("index.html", data)