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
    first_name: str
    last_name: str
    username: str
    email: str
    date_of_birth: date = Field(
        default=datetime.today, description='Дата в формате yyyy-mm-dd',
        examples=['2000-01-01',])
