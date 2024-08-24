from os import getenv
from datetime import datetime
from utils.data_utils import DataUtils
from services.base.HTTP_client import HTTPClient

class CurrenciesService(HTTPClient):
    def __init__(self):
        super().__init__(
            base_URL=getenv('CURRENCY_RATES_URL')
        )

    async def get_rates(self):
        params = DataUtils.obj_template
        params.fdate = datetime.now().strftime('%d.%m.%Y')
        return await self.get('/rss/get_rates.cfm', vars(params))