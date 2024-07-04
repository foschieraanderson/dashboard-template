from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.configs.database import db_session

from src.schemas.user_schema import UserResponse, UserSchema
from src.services.user_service import UserService

router = APIRouter()

@router.get("/")
async def users() -> str:
    return "tudo certo!"

@router.post("", status_code=201, response_model=UserResponse)
async def create_user(
        data: UserSchema,
        session: AsyncSession = Depends(db_session),
):
    _service = UserService(session)
    return await _service.create(data)
