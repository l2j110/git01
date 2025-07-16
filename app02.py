from pickletools import read_uint1
from fastapi import FastAPI

app = FastAPI()

# http://127.0.0.1:8002/items/all
@app.get("/items/all")
async def read_all_items():                 # async는 비동기 방식 지원
    return {"message" : "all_items"}

# http://127.0.0.1:8002/items/123
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id" : item_id}



# uvicorn 파일 이름: 객체 이름 --port-8002 --reroad
# uvicorn app_02:app --port=8002 --reload