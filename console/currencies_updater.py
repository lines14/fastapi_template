import xml.etree.ElementTree as ET
from utils.data_utils import DataUtils
from services.currencies_service import CurrenciesService

class CurrenciesUpdater:
    async def update(self) -> None:
        currencies = []
        currencies_service = CurrenciesService()
        response = await currencies_service.get_rates()
        root = ET.fromstring(response.text)
        for item in root.findall('item'):
            currency = DataUtils.obj_template
            currency.fullname = item.find('fullname').text
            currency.title = item.find('title').text
            currency.rate = float(item.find('description').text)
            currency.quant = int(item.find('quant').text)
            currency.index = item.find('index').text
            currency.change = float(item.find('change').text)
            currencies.append(currency)
        return [vars(obj) for obj in currencies]