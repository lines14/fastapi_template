import asyncio
import aioschedule
from typing import Annotated
from models.user import User
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse
from handlers.auth_handler import AuthHandler
from handlers.template_handler import TemplateHandler
from middlewares.auth_middleware import AuthMiddleware
from fastapi import FastAPI, Request, Response, Depends
from handlers.greetings_handler import GreetingsHandler
from handlers.registration_handler import RegistrationHandler
from scheduler.currency_rates_updater import CurrencyRatesUpdater

load_dotenv()

auth_handler = AuthHandler()
auth_middleware = AuthMiddleware()
template_handler = TemplateHandler()
greetings_handler = GreetingsHandler()
registration_handler = RegistrationHandler()
currency_rates_updater = CurrencyRatesUpdater()

async def start_scheduler():
    aioschedule.every().hour.at(":10").do(currency_rates_updater.update)
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
    redoc_url='/redoc',
    root_path='/api'
)

@app.get("/", response_class=HTMLResponse)
async def template(request: Request) -> Response:
    return await template_handler.template(request)

@app.post('/registration')
async def registration(user: Annotated[User, Depends()]) -> Response:
    return await registration_handler.registration(user)

@app.post('/auth')
async def auth(request: Request, user: Annotated[User, Depends()]) -> Response:
    return await auth_handler.auth(request, user)

@app.get('/greetings')
@auth_middleware.check_bearer_token
async def greetings() -> Response:
    return await greetings_handler.greetings()