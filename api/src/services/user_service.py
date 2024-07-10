from typing import List, Optional
from pydantic import UUID4
from src.providers.security import password_hash
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.user_repository import UserRepository
from src.schemas.user_schema import UserResponse, UserSchema


class UserService:
    "User Service Class"
    def __init__(self, session: AsyncSession):
        self.repository = UserRepository(session)

    async def create(self, data: UserSchema) -> UserResponse:
        user = data.copy()
        user.password = password_hash(data.password)
        return await self.repository.create(user)

    async def get_all(self) -> List[Optional[UserResponse]]:
        return await self.repository.get_all()

    async def get_by_id(self, _id: UUID4) -> UserResponse:
        return await self.repository.get_by_id(_id)
