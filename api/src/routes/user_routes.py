from typing import List
from pydantic import UUID4
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.configs.database import db_session

from src.schemas.user_schema import UserResponse, UserSchema
from src.services.user_service import UserService

router = APIRouter()

@router.get("", status_code=status.HTTP_200_OK, response_model=List[UserResponse])
async def get_users(session: AsyncSession = Depends(db_session)) -> List[UserResponse]:
    _service = UserService(session)
    return await _service.get_all()

@router.get("/{_id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user_by_id(_id: UUID4, session: AsyncSession = Depends(db_session)) -> UserResponse:
    _service = UserService(session)
    return await _service.get_by_id(_id)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(
        data: UserSchema,
        session: AsyncSession = Depends(db_session),
) -> UserResponse:
    _service = UserService(session)
    return await _service.create(data)
