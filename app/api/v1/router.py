from fastapi import APIRouter

from .endpoints import category, user

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user", tags=["User"])
api_router.include_router(
    category.router, prefix="/category", tags=["Category"])
