from fastapi import Body
# from pydantic import Field
from typing import Annotated

Login = Annotated[str, Body(title='Логин пользователя сервиса', min_length=4, max_length=20)]
Password = Annotated[str, Body(title='Пароль пользователя сервиса', min_length=6, max_length=100)]