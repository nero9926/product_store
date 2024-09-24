from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from pydantic import UUID4
from sqlalchemy.orm import Session

import app.services.user as service
from app.api.deps import get_db_pg
from app.models.user import User
from app.schemas.user import UserIn, UserOut

router = APIRouter()


@router.post(
    "/create",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
    summary="Создает пользователя",
)
def create_user(
    user: Annotated[UserIn, Depends()],
    db: Session = Depends(get_db_pg),
) -> UserOut:
    return service.create_user(
        db=db,
        user=user,
    )


@router.get(
    "/get",
    status_code=status.HTTP_200_OK,
    response_model=List[UserOut],
    summary="Возвращает всех пользователей",
)
async def get_all_users(
    db: Session = Depends(get_db_pg),
) -> List[User]:
    """
    # Ответ:
    | Параметр | Тип | Описание |
    |----------|-----|----------|
    | id | int | id страны. |
    | name | str | Название страны. |
    ```
    [
      {
        "id": 1,
        "name": "USA"
      },
      {
        "id": 2,
        "name": "Russia"
      }
    ]
    ```
    """

    return service.get_all_users(db=db)


@router.get(
    "/get/{user_uuid}",
    status_code=status.HTTP_200_OK,
    response_model=UserOut,
    summary="Возвращает пользователя по uuid",
)
async def get_user(
    user_uuid: UUID4,
    db: Session = Depends(get_db_pg),
) -> List[User]:
    """

    """

    return service.get_user(user_uuid=user_uuid, db=db)
