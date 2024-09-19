from typing import List

from psycopg2 import errors as pg_errors
from pydantic import UUID4
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import app.db.base as models
from app.exceptions.shop import ShopAlreadyExists
from app.schemas.shop import ShopIn, ShopOut


def create_shop(db: Session, shop: ShopIn) -> ShopOut:
    db_shop = models.Shop(**shop.dict())
    try:
        models.save(db=db, data=db_shop)
    except IntegrityError as e:
        print(e)
        if isinstance(e.orig, pg_errors.UniqueViolation):
            raise ShopAlreadyExists("Shop already exists")
        raise

    return ShopOut(**db_shop.__dict__)


def get_all_shops(db: Session) -> List[ShopOut]:
    all_shops = db.query(models.Shop).all()
    # print(TypeAdapter(List[ShopOut]).dump_python(all_users))
    return [ShopOut(**shop.__dict__) for shop in all_shops]


def get_shop(shop_uuid: UUID4, db: Session) -> List[ShopOut]:
    shop = db.query(models.Shop).get({"id": shop_uuid})
    return ShopOut(**shop.__dict__)
