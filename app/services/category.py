from typing import List

from psycopg2 import errors as pg_errors
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import app.db.base as models
from app.exceptions.category import CategoryAlreadyExists
from app.schemas.category import CategoryIn, CategoryOut


def create_category(db: Session, category: CategoryIn) -> CategoryOut:
    db_category = models.Category(**category.dict())
    try:
        models.save(db=db, data=db_category)
    except IntegrityError as e:
        print(e)
        if isinstance(e.orig, pg_errors.UniqueViolation):
            raise CategoryAlreadyExists("Category already exists")
        raise

    return CategoryOut(**db_category.__dict__)


def get_all_categories(db: Session) -> List[CategoryOut]:
    all_categories = db.query(models.Category).all()
    # print(TypeAdapter(List[CategoryOut]).dump_python(all_users))
    return [CategoryOut(**category.__dict__) for category in all_categories]


def get_category(category_id: int, db: Session) -> List[CategoryOut]:
    category = db.query(models.Category).get({"id": category_id})
    return CategoryOut(**category.__dict__)
