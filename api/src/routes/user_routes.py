from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def users() -> str:
    return "tudo certo!"
