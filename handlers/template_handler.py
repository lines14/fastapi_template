from sys import version
from fastapi import Request, __version__
from fastapi.templating import Jinja2Templates

class TemplateHandler:
    async def template(self, request: Request) -> str:
        data = {
            'request': request,
            'pythonVersion': version,
            'fastapiVersion': __version__
        }

        templates = Jinja2Templates(directory="../templates")
        return templates.TemplateResponse("index.html", data)