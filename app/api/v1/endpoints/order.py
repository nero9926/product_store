from typing import List

from fastapi import APIRouter, Depends, status
from pydantic import UUID4
from sqlalchemy.orm import Session

import app.services.order as service
from app.api.deps import get_db_pg
# from app.broker.base import mq
from app.models.order import Order
from app.schemas.order import OrderIn, OrderOut

router = APIRouter()


@router.post(
    "/create",
    response_model=OrderOut,
    status_code=status.HTTP_201_CREATED,
    summary="Создает заказ",
)
def create_order(
    order: OrderIn,
    db: Session = Depends(get_db_pg),
) -> dict:
    created_order = service.create_order(
        db=db,
        order=order,
    )
    # send to RMQ
    # mq.send_notification(
    #     {
    #         'order_uuid': created_order.id,
    #         'order_status': created_order.status,
    #         'deliver_date': created_order.deliver_date,
    #         'total': created_order.total,
    #     }
    # )
    # mq.send_order(
    #     {
    #         'order_uuid': created_order.id,
    #     }
    # )
    return created_order


@router.get(
    "/get",
    status_code=status.HTTP_200_OK,
    response_model=List[OrderOut],
    summary="Возвращает все заказы",
)
async def get_all_orders(
    db: Session = Depends(get_db_pg),
) -> List[Order]:
    return service.get_all_orders(db=db)


@router.get(
    "/get/{order_uuid}",
    status_code=status.HTTP_200_OK,
    response_model=OrderOut,
    summary="Возвращает заказ по uuid",
)
async def get_order(
    order_uuid: UUID4,
    db: Session = Depends(get_db_pg),
) -> List[Order]:
    return service.get_order(order_uuid=order_uuid, db=db)
