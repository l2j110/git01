from fastapi import FastAPI

app = FastAPI()

# http://127.0.0.8002/
@app.get("/")   #    ^
#         |          |
#         ㄴ---------ㅓ
def root():
    return {"message" : "nice to meet you world"}

# http://127.0.0.8002/item
@app.get("/item")
def get_item():
    return {"item" : "item으로 들어왔군요"}

# http://127.0.0.8002/items/2
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id" : f"{item_id}로 들어왔군요"}


# uvicorn 파일 이름: 객체 이름 --port-8002 --reroad
# uvicorn app_01:app --port=8002 --reload