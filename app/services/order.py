from typing import List

from psycopg2 import errors as pg_errors
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import app.db.base as models
from app.exceptions.order import OrderAlreadyExists
from app.schemas.order import OrderIn, OrderOut


def create_order(db: Session, order: OrderIn) -> OrderOut:
    total = 0
    for product_uuid in order.products_ids:
        product_db = db.query(models.Product).get({"id": product_uuid})
        total += product_db.price
    order_dict = order.model_dump()
    order_dict["total"] = total
    del order_dict['products_ids']
    db_order = models.Order(**order_dict)
    try:
        models.save(db=db, data=db_order)
        for product_uuid in order.products_ids:
            product_db = db.query(models.Product).get({"id": product_uuid})
            order_products = {
                "order_id": db_order.id,
                "product_id": product_db.id,
                "quantity": 1
            }
            db_order_products = models.Order_Product(**order_products)
            models.save(db=db, data=db_order_products)

    except IntegrityError as e:
        print(e)
        if isinstance(e.orig, pg_errors.UniqueViolation):
            raise OrderAlreadyExists("Order already exists")
        raise

    return db_order


def get_all_orders(db: Session) -> List[OrderOut]:
    all_orders = db.query(models.Order).all()
    # print(TypeAdapter(List[OrderOut]).dump_python(all_users))
    return [order for order in all_orders]


def get_order(order_id: int, db: Session) -> List[OrderOut]:
    order = db.query(models.Order).get({"id": order_id})
    return order


def patch_order(order_id: int, payload: dict, db: Session) -> List[OrderOut]:
    order_db = db.query(models.Order).get({"id": order_id})
    updated_item = order_db.copy(update=payload)
    models.save(db=db, data=updated_item)
    return updated_item
