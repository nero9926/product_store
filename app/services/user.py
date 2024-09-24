from typing import List

from psycopg2 import errors as pg_errors
from pydantic import UUID4, TypeAdapter
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import app.db.base as models
from app.exceptions.user import UserAlreadyExists
from app.schemas.user import UserIn, UserOut


def create_user(db: Session, user: UserIn) -> UserOut:
    db_user = models.User(**user.model_dump())
    try:
        models.save(db=db, data=db_user)
    except IntegrityError as e:
        print(e)
        if isinstance(e.orig, pg_errors.UniqueViolation):
            raise UserAlreadyExists("User already exists")
        raise

    return db_user


def get_all_users(db: Session) -> List[UserOut]:
    all_users = db.query(models.User).all()
    return [user for user in all_users]


def get_user(user_uuid: UUID4, db: Session) -> List[UserOut]:
    user = db.query(models.User).get({"id": user_uuid})
    return user
