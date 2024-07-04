from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.user_repository import UserRepository
from src.schemas.user_schema import UserResponse, UserSchema


class UserService:
    "User Service Class"
    def __init__(self, session: AsyncSession):
        self.repository = UserRepository(session)

    async def create(self, data: UserSchema) -> UserResponse:
        return await self.repository.create(data)
