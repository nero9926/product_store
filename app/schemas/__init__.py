
from pydantic import BaseModel

from app.schemas.user import *


class BaseSchema(BaseModel):
    class Config:
        orm_mode = True
