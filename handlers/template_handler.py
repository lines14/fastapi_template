import traceback
from sys import version
from utils.logger import Logger
from fastapi.templating import Jinja2Templates
from utils.response_utils import ResponseUtils
from fastapi import Request, Response, __version__
from DTO import ResponseTemplateDTO, ResponseTemplateContextDTO

class TemplateHandler:
    async def template(self, request: Request) -> Response:
        try:
            data = ResponseTemplateContextDTO(
                request=request, 
                pythonVersion=version, 
                fastapiVersion=__version__
            )
            templates = Jinja2Templates(directory="../templates")
            template = templates.TemplateResponse("index.html", vars(data))
            ResponseTemplateDTO(**vars(template))
            return template
        except Exception as e:
            Logger.log(traceback.format_exc())
            return await ResponseUtils.error(str(e))