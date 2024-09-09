from typing import List

# from psycopg2 import errors as pg_errors
from pydantic import TypeAdapter
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import app.db.base as models
from app import schemas

# from app.exceptions.country import CountryAlreadyExists


def create_user(db: Session, user):
    db_user = models.User(**user.dict())
    try:
        models.save(db=db, data=db_user)
    except IntegrityError as e:
        print(e)
        # if isinstance(e.orig, pg_errors.UniqueViolation):
        #     raise CountryAlreadyExists("Country already exists")
        # raise

    return schemas.UserOut(**db_user.__dict__)


def get_all_users(db: Session) -> List[schemas.UserOut]:
    all_users = db.query(models.User).all()

    return TypeAdapter.validate_python(List[schemas.CountryOut], all_users)
