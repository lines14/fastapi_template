from sys import version
from utils.data_utils import DataUtils
from fastapi import Request, __version__
from fastapi.templating import Jinja2Templates

class TemplateHandler:
    async def template(self, request: Request) -> str:
        data = DataUtils.obj_template
        data.request = request
        data.pythonVersion = version
        data.fastapiVersion = __version__
        templates = Jinja2Templates(directory="../templates")
        return templates.TemplateResponse("index.html", vars(data))