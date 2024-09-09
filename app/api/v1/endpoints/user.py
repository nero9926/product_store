from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import app.services.user as service
from app.api.deps import get_db_pg
from app.models.user import User
from app.schemas.user import UserIn, UserOut

router = APIRouter()


@router.post(
    "/",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
    summary="Создает пользователя",
)
def create_user(
    user: UserIn,
    db: Session = Depends(get_db_pg),
) -> UserOut:
    """
    # Ответ:
    | Параметр | Тип | Описание |
    |----------|-----|----------|
    | id | int | id страны. |
    | name | str | Название страны. |
    ```
    {
        "id": 1,
        "name": "Russia"
    }
    ```
    """
    return service.create_user(
        db=db,
        user=user,
    )


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[UserOut],
    summary="Возвращает все страны",
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
