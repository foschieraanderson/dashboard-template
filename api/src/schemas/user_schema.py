from pydantic import UUID4, BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    uuid: UUID4
    email: EmailStr
    username: str
