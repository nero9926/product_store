from datetime import date, datetime

from pydantic import Field

from app.schemas import BaseSchema


class UserOut(BaseSchema):
    id: int
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
