from fastapi import APIRouter
from pydantic import BaseModel


# http://127.0.0.1:8002/item
router = APIRouter(prefix="/user", tags=["item"])

@router.get("/")
async def read_users():
    return [{"username": "홍길동"}, {"username": "김길동"}]