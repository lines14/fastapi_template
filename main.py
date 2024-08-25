import asyncio
import aioschedule
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse
from handlers.auth_handler import AuthHandler
from handlers.template_handler import TemplateHandler
from middlewares.auth_middleware import AuthMiddleware
from handlers.greetings_handler import GreetingsHandler
from scheduler.currency_rates_updater import CurrencyRatesUpdater

load_dotenv()

auth_handler = AuthHandler()
auth_middleware = AuthMiddleware()
template_handler = TemplateHandler()
greetings_handler = GreetingsHandler()
currency_rates_updater = CurrencyRatesUpdater()

async def start_scheduler():
    aioschedule.every().hour.do(currency_rates_updater.update)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
        
@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(start_scheduler())
    yield

app = FastAPI(
    lifespan=lifespan,
    title='Spending tracker API',
    docs_url='/docs',
    root_path='/api'
)

@app.get("/", response_class=HTMLResponse)
async def template(request: Request) -> str:
    return await template_handler.template(request)

@app.post('/auth')
async def auth(request: Request) -> str:
    return await auth_handler.auth(request)

@app.get('/greetings')
@auth_middleware.check_bearer_token
async def greetings(request: Request) -> str:
    return await greetings_handler.greetings(request)

# @app.post('/create')
# @auth_middleware.check_bearer_token
# async def post(request: Request) -> str:
#     return await example_handler.post(request)