import random
import string
from typing import List

from psycopg2 import errors as pg_errors
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import app.db.base as models
from app.exceptions.product import ProductAlreadyExists
from app.schemas.product import ProductIn, ProductOut


def create_product(db: Session, product: ProductIn) -> ProductOut:

    db_product = models.Product(**product.model_dump())
    try:
        models.save(db=db, data=db_product)
        sku = ''.join(random.choices(
            string.ascii_letters + string.digits, k=16))
        sku_dict = {
            "sku": sku,
            "quantity": 0,
            "product_id": db_product.id
        }
        db_product_sku = models.ProductSku(**sku_dict)
        models.save(db=db, data=db_product_sku)
    except IntegrityError as e:
        print(e)
        if isinstance(e.orig, pg_errors.UniqueViolation):
            raise ProductAlreadyExists("Product already exists")
        raise

    return db_product


def get_all_products(db: Session) -> List[ProductOut]:
    all_products = db.query(models.Product).all()
    # print(TypeAdapter(List[ProductOut]).dump_python(all_users))
    return [product for product in all_products]


def get_product(product_id: int, db: Session) -> List[ProductOut]:
    product = db.query(models.Product).get({"id": product_id})
    return product
