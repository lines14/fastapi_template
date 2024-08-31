from typing import List, Type
from sqlmodel import SQLModel
from fastapi import HTTPException, Request
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, ValidationError, create_model

def validate(cls: Type[BaseModel], fields: List[str]):
    async def validate_fields(request: Request) -> BaseModel:
        errors = []
        validated_data = {}
        data = await request.json()
        for field in fields:
            if field in data:
                try:
                    SingleFieldModel = create_model('SingleFieldModel', **{field: (cls.__annotations__[field], ...)})
                    validated_field = SingleFieldModel(**{field: data[field]})
                    validated_data[field] = validated_field.dict()[field]
                except ValidationError as e:
                    errors.extend(e.errors())
            else:
                errors.append({
                    "type": "missing",
                    "loc": ["body", field],
                    "msg": "Field required",
                    "input": None
                })
        if errors:
            raise HTTPException(422, detail=errors)
        return cls(**validated_data)
    return validate_fields

class BaseModel(SQLModel):
    class Config:
        validate_assignment = True
        arbitrary_types_allowed=True