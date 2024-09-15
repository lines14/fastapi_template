import traceback
from DTO import PurchaseDTO
from models import Purchase
from fastapi import Response
from utils.logger import Logger
from utils.data_utils import DataUtils
from utils.response_utils import ResponseUtils

class PurchaseHandler:
    async def create_purchase(self, purchase: PurchaseDTO) -> Response:
        try:
            new_purchase = Purchase(
                cost=purchase.cost, 
                account_id=purchase.account_id,
                sub_type_id=purchase.sub_type_id,
            )
            await new_purchase.create()
            return await ResponseUtils.success(DataUtils.responses.purchase_created_message)
        except Exception as e:
            Logger.log(traceback.format_exc())
            return await ResponseUtils.error(str(e))