from fastapi import APIRouter
from pydantic import BaseModel


# http://127.0.0.1:8002/item
router = APIRouter(prefix="/item", tags=["item"])


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# http://127.0.0.1:8002/item/2
# 그니까 router 얘가 그냥 http://127.0.0.1:8002/item 라는 거
@router.get("/{item_id}")
async def read_item(item_id: int):
    return {'item_id': item_id}