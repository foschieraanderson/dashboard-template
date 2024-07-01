from fastapi import APIRouter
from src.routes import user_routes

router = APIRouter()

router.include_router(user_routes.router, tags=["users"], prefix="/users")

