from datetime import datetime
from typing import List, Optional

from pydantic import UUID4, Field

from app.models.order import Order
from app.schemas import BaseSchema


class OrderOut(BaseSchema):
    id: UUID4
    customer_id: UUID4
    total: float
    date_placed: datetime
    deliver_date: datetime
    products: Optional[List[UUID4]]
    payment_details_id: Optional[UUID4]


class OrderIn(BaseSchema):
    id: UUID4 = Field()
    customer_id: UUID4 = Field()
    total: float = Field()
    date_placed: datetime = Field()
    deliver_date: datetime = Field()
    products: Optional[List[UUID4]] = Field()
    payment_details_id: Optional[UUID4] = Field()
