from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import app.services.category as service
from app.api.deps import get_db_pg
from app.models.category import Category
from app.schemas.category import CategoryIn, CategoryOut

router = APIRouter()


@router.post(
    "/create",
    response_model=CategoryOut,
    status_code=status.HTTP_201_CREATED,
    summary="Создает категорию",
)
def create_category(
    category: Annotated[CategoryIn, Depends()],
    db: Session = Depends(get_db_pg),
) -> CategoryOut:

    return service.create_category(
        db=db,
        category=category,
    )


@router.get(
    "/get",
    status_code=status.HTTP_200_OK,
    response_model=List[CategoryOut],
    summary="Возвращает все категории",
)
async def get_all_categories(
    db: Session = Depends(get_db_pg),
) -> List[Category]:

    return service.get_all_categories(db=db)


@router.get(
    "/get/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=CategoryOut,
    summary="Возвращает категорию по id",
)
async def get_category(
    category_id: int,
    db: Session = Depends(get_db_pg),
) -> List[Category]:
    return service.get_category(category_id=category_id, db=db)
