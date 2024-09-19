from typing import List

from fastapi import APIRouter, Depends, status
from pydantic import UUID4
from sqlalchemy.orm import Session

import app.services.shop as service
from app.api.deps import get_db_pg
from app.models.shop import Shop
from app.schemas.shop import ShopIn, ShopOut

router = APIRouter()


@router.post(
    "/create",
    response_model=ShopOut,
    status_code=status.HTTP_201_CREATED,
    summary="Создает магазин",
)
def create_shop(
    shop: ShopIn,
    db: Session = Depends(get_db_pg),
) -> ShopOut:
    return service.create_shop(
        db=db,
        shop=shop,
    )


@router.get(
    "/get",
    status_code=status.HTTP_200_OK,
    response_model=List[ShopOut],
    summary="Возвращает все магазины",
)
async def get_all_shops(
    db: Session = Depends(get_db_pg),
) -> List[Shop]:
    return service.get_all_shops(db=db)


@router.get(
    "/get/{shop_id}",
    status_code=status.HTTP_200_OK,
    response_model=ShopOut,
    summary="Возвращает магазин по uuid",
)
async def get_shop(
    shop_uuid: UUID4,
    db: Session = Depends(get_db_pg),
) -> List[Shop]:
    return service.get_shop(shop_uuid=shop_uuid, db=db)
