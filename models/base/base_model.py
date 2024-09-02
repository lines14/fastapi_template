from typing import Type, List
from sqlmodel import SQLModel
from fastapi import HTTPException, Request
from database.base.database import Database
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, ValidationError, create_model

class BaseModel(SQLModel):
    async def create(self):
        async with Database() as database:
            await database.create(self)

    async def get(self):
        async with Database() as database:
            return await database.get(self)
        
    async def get_all(self):
        async with Database() as database:
            return await database.get_all(self)

    @classmethod
    def validate(cls: Type[BaseModel], fields: List[str]):
        async def validate_fields(request: Request) -> BaseModel:
            errors = []
            validated_data = {}
            data = await request.json()
            for field in fields:
                if field in data:
                    try:
                        SingleFieldModel = create_model(
                            'SingleFieldModel', 
                            **{field: (cls.__annotations__[field], ...)}
                        )
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

    class Config:
        validate_assignment = True
        arbitrary_types_allowed=True