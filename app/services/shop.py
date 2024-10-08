from typing import List

from psycopg2 import errors as pg_errors
from pydantic import UUID4
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import app.db.base as models
from app.exceptions.shop import ShopAlreadyExists
from app.schemas.shop import ShopIn, ShopOut


def create_shop(db: Session, shop: ShopIn) -> ShopOut:
    db_shop = models.Shop(**shop.model_dump())
    try:
        models.save(db=db, data=db_shop)
    except IntegrityError as e:
        print(e)
        if isinstance(e.orig, pg_errors.UniqueViolation):
            raise ShopAlreadyExists("Shop already exists")
        raise

    return db_shop


def get_all_shops(db: Session) -> List[ShopOut]:
    all_shops = db.query(models.Shop).all()
    return [shop for shop in all_shops]


def get_shop(shop_uuid: UUID4, db: Session) -> List[ShopOut]:
    shop = db.query(models.Shop).get({"id": shop_uuid})
    return shop
