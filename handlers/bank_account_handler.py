import traceback
from fastapi import Response
from DTO import BankAccountDTO
from models import BankAccount
from utils.logger import Logger
from utils.data_utils import DataUtils
from utils.response_utils import ResponseUtils

class BankAccountHandler:
    async def create_bank_account(self, bank_account: BankAccountDTO) -> Response:
        try:
            new_bank_account = BankAccount(
                account=bank_account.account, 
                issuer_id=bank_account.issuer_id,
                currency_id=bank_account.currency_id,
                user_id=bank_account.user_id
            )
            await new_bank_account.create()
            return await ResponseUtils.success(DataUtils.responses.bank_account_created_message)
        except Exception as e:
            Logger.log(traceback.format_exc())
            return await ResponseUtils.error(str(e))