from sqlalchemy.ext.asyncio import AsyncSession
from src.models.user_model import User

from src.schemas.user_schema import UserResponse, UserSchema


class UserRepository:
    """User Repository Class"""
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: UserSchema) -> UserResponse:
        """Create new user"""
        user = User(**data.model_dump(exclude_none=True))
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return UserResponse(**user.__dict__)

