from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from pydantic import UUID4
from sqlalchemy.orm import Session

import app.services.product as service
from app.api.deps import get_db_pg
from app.models.product import Product
from app.schemas.product import ProductIn, ProductOut

router = APIRouter()


@router.post(
    "/create",
    response_model=ProductOut,
    status_code=status.HTTP_201_CREATED,
    summary="Создает товар",
)
def create_product(
    product: Annotated[ProductIn, Depends()],
    db: Session = Depends(get_db_pg),
) -> ProductOut:
    return service.create_product(
        db=db,
        product=product,
    )


@router.get(
    "/get",
    status_code=status.HTTP_200_OK,
    response_model=List[ProductOut],
    summary="Возвращает все товары",
)
async def get_all_products(
    db: Session = Depends(get_db_pg),
) -> List[Product]:
    return service.get_all_products(db=db)


@router.get(
    "/get/{product_uuid}",
    status_code=status.HTTP_200_OK,
    response_model=ProductOut,
    summary="Возвращает товар по uuid",
)
async def get_product(
    product_uuid: UUID4,
    db: Session = Depends(get_db_pg),
) -> List[Product]:
    return service.get_product(product_uuid=product_uuid, db=db)
