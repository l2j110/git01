from fastapi import FastAPI, Request

app = FastAPI()

# --------------------------------
# http://127.0.0.1:8002/items
# --------------------------------

@app.get("/items")
async def read_item(request: Request):
    client_host = request.client.host       # 대충 내 아이피 주소
    headers = request.headers
    query_params = request.query_params
    url = request.url
    path_params = request.path_params
    http_method = request.method

    return {
        "client_host" : client_host,
        "headers" : headers,
        "query_params" : query_params,
        "url" : url,
        "path_params" : path_params,
        "http_method" : http_method
    }

# uvicorn app_04:app --port=8002 --reload