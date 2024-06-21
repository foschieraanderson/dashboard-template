from fastapi import APIRouter
from src.routes import users

router = APIRouter()

router.include_router(users.router, tags=["users"], prefix="/users")

