import asyncio
import aioschedule
from dotenv import load_dotenv
from models.user import Login, Password
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse
from handlers.auth_handler import AuthHandler
from fastapi import FastAPI, Request, Response
from handlers.template_handler import TemplateHandler
from middlewares.auth_middleware import AuthMiddleware
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
async def registration(request: Request, login: Login, password: Password) -> Response:
    return await registration_handler.registration(request)

@app.post('/auth')
async def auth(request: Request, login: Login, password: Password) -> Response:
    return await auth_handler.auth(request)

@app.get('/greetings')
@auth_middleware.check_bearer_token
async def greetings(request: Request) -> Response:
    return await greetings_handler.greetings(request)