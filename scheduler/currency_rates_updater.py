import os
import sys
sys.path.append(os.getcwd())
from dotenv import load_dotenv
import xml.etree.ElementTree as ET
from utils.data_utils import DataUtils
from models import Currency, CurrencyRate
from database.base.database import Database
from services.currencies_service import CurrenciesService

load_dotenv()

class CurrencyRatesUpdater:
    async def update(self) -> None:
        currency_rates = []
        currencies_service = CurrenciesService()
        response = await currencies_service.get_rates()
        root = ET.fromstring(response.text)
        for item in root.findall('item'):
            currency_rate = DataUtils.obj_template
            currency_rate.title = item.find('title').text
            currency_rate.rate = float(item.find('description').text)
            currency_rates.append(currency_rate)
        titles = list(map(lambda title: title[0], database.get_all(Currency.currency)))
        currency_rates = list(filter(lambda currency_rate: currency_rate.title in titles, currency_rates))
        currency_rates = sorted(currency_rates, key=lambda currency_rate: titles.index(currency_rate.title))
        currency_rates_models = list(map(lambda currency_rate: CurrencyRate(currency_id=database
                            .get(Currency(currency=currency_rate.title)).id, rate=currency_rate.rate), currency_rates))
        database = Database()
        database.seed([
            CurrencyRate(currency_id=database.get(Currency(currency='KZT')).id, rate=1),
            *currency_rates_models
        ])
        print(f'INFO:     Successfully updated currency rates')