from dotenv import load_dotenv
# from middlewares.auth import bearer_token
from handlers.example_handler import ExampleHandler
from handlers.template_handler import TemplateHandler
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

load_dotenv()
app = FastAPI()
example_handler = ExampleHandler()
template_handler = TemplateHandler()

@app.get("/", response_class=HTMLResponse)
async def template(request: Request) -> str:
    return await template_handler.template(request)

# Api routes
@app.post('/example')
# @bearer_token
async def example(request: Request) -> str:
    return await example_handler.example(request)