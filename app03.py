import http
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name":"자장면"},{"item_name":"짬뽕"}, {"item_name":"탕수육"}]


# path 파라미터  : http://127.0.0.1:8002/items/all
#               : http://127.0.0.1:8002/items/123
#
# query 파라미터 : # http://127.0.0.1:8002/items?start=1&end=3
# (물음표)


# http:127.0.0.1:8002/items?start=0&end=2
@app.get("/items")
async def read_item(start: int=0, end: int=2):
    return fake_items_db[start : end+1]

# http://127.0.0.1:8002/items_nd?start=0&end=2    
@app.get("/items_nd/")
async def itens_nd(start: int=0, end: int=2):
    return fake_items_db[start:start+end]


# uvicorn 파일 이름: 객체 이름 --port-8002 --reroad
# uvicorn app_03:app --port=8002 --reload