from typing import ClassVar
from utils.data_utils import DataUtils
from pydantic import Field, model_validator
from DTO.base import BaseDTO, FloatValidator, IntegerValidator

class PurchaseDTO(BaseDTO):
    min_value_currency_id: ClassVar[int] = 1
    max_value_currency_id: ClassVar[int] = 4
    min_value_cost: ClassVar[int] = 0.01
    max_value_cost: ClassVar[int] = 10000000
    min_value_sub_type_id: ClassVar[int] = 1
    max_value_sub_type_id: ClassVar[int] = 108

    cost: float = Field(
        default=..., 
        description=DataUtils.responses.cost_validation_message,
        ge=min_value_cost, 
        le=max_value_cost
    )
    sub_type_id: int = Field(
        default=..., 
        description=DataUtils.responses.sub_type_id_validation_message,
        ge=min_value_sub_type_id, 
        le=max_value_sub_type_id
    )
    currency_id: int = Field(
        default=..., 
        description=DataUtils.responses.currency_id_validation_message,
        ge=min_value_currency_id, 
        le=max_value_currency_id
    )

    @model_validator(mode="after")
    @classmethod
    def validate_fields(cls, values):
        cost = FloatValidator(values.cost)
        sub_type_id = IntegerValidator(values.sub_type_id)
        currency_id = IntegerValidator(values.currency_id)
        if not cost.has_two_decimal_places() and not cost.is_in_range(cls.min_value_cost, cls.max_value_cost):
            raise ValueError(DataUtils.responses.cost_validation_message)
        if not sub_type_id.is_in_range(cls.min_value_sub_type_id, cls.max_value_sub_type_id):
            raise ValueError(DataUtils.responses.sub_type_id_validation_message)
        if not currency_id.is_in_range(cls.min_value_currency_id, cls.max_value_currency_id):
            raise ValueError(DataUtils.responses.currency_id_validation_message)
        return values