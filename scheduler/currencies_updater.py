import xml.etree.ElementTree as ET
from utils.data_utils import DataUtils
from database.database import Database
from models import Currency, CurrencyRate
from services.currencies_service import CurrenciesService

class CurrenciesUpdater:
    async def update(self) -> None:
        currencies = []
        database = Database()
        currencies_service = CurrenciesService()
        response = await currencies_service.get_rates()
        root = ET.fromstring(response.text)
        for item in root.findall('item'):
            currency = DataUtils.obj_template
            currency.title = item.find('title').text
            currency.rate = float(item.find('description').text)
            currencies.append(currency)
        titles = list(map(lambda title: title[0], database.get_all(Currency.currency)))
        currencies = list(filter(lambda currency: currency.title in titles, currencies))
        currencies = sorted(currencies, key=lambda currency: titles.index(currency.title))
        currency_models = list(map(lambda currency: CurrencyRate(currency_id=database
                            .get(Currency(currency=currency.title)).id, rate=currency.rate), currencies))
        database.seed([
            CurrencyRate(currency_id=database.get(Currency(currency='KZT')).id, rate=1),
            *currency_models
        ])