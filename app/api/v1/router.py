from fastapi import APIRouter

from .endpoints import category, order, product, shop, user

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user", tags=["User"])
api_router.include_router(
    category.router, prefix="/category", tags=["Category"])
api_router.include_router(shop.router, prefix="/shop", tags=["Shop"])
api_router.include_router(product.router, prefix="/product", tags=["Product"])
api_router.include_router(order.router, prefix="/order", tags=["Order"])
