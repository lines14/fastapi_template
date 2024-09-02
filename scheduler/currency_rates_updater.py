import os
import sys
sys.path.append(os.getcwd())
from dotenv import load_dotenv
import xml.etree.ElementTree as ET
from DTO import CurrencyRateResponseDTO
from models import Currency, CurrencyRate
from database.base.database import Database
from services.currencies_service import CurrenciesService

load_dotenv()

class CurrencyRatesUpdater:
    async def update(self) -> None:
        currency_rates = []
        response = await CurrenciesService().get_rates()
        root = ET.fromstring(response.text)
        for item in root.findall('item'):
            currency_rate = CurrencyRateResponseDTO(
                title=item.find('title').text, 
                rate=float(item.find('description').text)
            )
            currency_rates.append(currency_rate)
        currency_titles = list(map(lambda currency: currency.currency, await Currency().get_all()))
        currency_rates = list(filter(lambda currency_rate: currency_rate.title in currency_titles, currency_rates))
        currency_rates = sorted(currency_rates, key=lambda currency_rate: currency_titles.index(currency_rate.title))
        currency_rates_models = []
        for currency_rate in currency_rates:
            currency_rates_models.append(CurrencyRate(currency_id=(await Currency(currency=currency_rate.title).get()).id, 
                                                      rate=currency_rate.rate))
        async with Database() as database:
            await database.seed([
                CurrencyRate(currency_id=(await Currency(currency='KZT').get()).id, rate=1),
                *currency_rates_models
            ])
        print(f'INFO:     Successfully updated currency rates')