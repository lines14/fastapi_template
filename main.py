from dotenv import load_dotenv
# from middlewares.auth import bearer_token
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from handlers.template_handler import TemplateHandler
from handlers.welcome_handler import WelcomeHandler

template_handler = TemplateHandler()
welcome_handler = WelcomeHandler()
app = FastAPI()
load_dotenv()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> str:
    return welcome_handler.welcome(request)

# Api routes
@app.post('/template')
# @bearer_token
async def template(request: Request) -> str:
    return template_handler.template(request)