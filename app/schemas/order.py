from datetime import datetime
from typing import List, Optional

from pydantic import UUID4, Field

from app.schemas import BaseSchema
from app.schemas.order_product import OrderProductOut


class OrderOut(BaseSchema):
    id: UUID4
    customer_id: UUID4
    total: float
    date_placed: datetime
    deliver_date: datetime
    products: Optional[List[OrderProductOut]]
    payment_details_id: Optional[UUID4]


class OrderIn(BaseSchema):
    customer_id: UUID4
    products_ids: List[UUID4]
