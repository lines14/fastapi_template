from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from handlers.auth_handler import AuthHandler
from handlers.example_handler import ExampleHandler
from handlers.template_handler import TemplateHandler
from middlewares.auth_middleware import AuthMiddleware

load_dotenv()
app = FastAPI()
auth_handler = AuthHandler()
auth_middleware = AuthMiddleware()
example_handler = ExampleHandler()
template_handler = TemplateHandler()

@app.get("/", response_class=HTMLResponse)
async def template(request: Request) -> str:
    return await template_handler.template(request)

@app.post('/auth')
async def auth(request: Request) -> str:
    return await auth_handler.auth(request)

@app.get('/get')
@auth_middleware.check_bearer_token
async def get(request: Request) -> str:
    return await example_handler.get(request)

@app.post('/post')
@auth_middleware.check_bearer_token
async def post(request: Request) -> str:
    return await example_handler.post(request)