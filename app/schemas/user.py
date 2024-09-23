from datetime import date, datetime
from typing import Optional

from pydantic import UUID4, Field

from app.schemas import BaseSchema
from app.schemas.shop import ShopOut


class UserOut(BaseSchema):
    id: UUID4
    first_name: str
    last_name: str
    username: str
    email: str
    # shops: Optional[ShopOut]


class UserOutMin(BaseSchema):
    id: UUID4
    first_name: str
    last_name: str
    username: str
    email: str


class UserIn(BaseSchema):
    first_name: str = Field(default="name")
    last_name: str = Field(default="surname")
    username: str = Field(default="username")
    email: str = Field(default="email@email.ru")
    date_of_birth: date = Field(default=datetime.today)
