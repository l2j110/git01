from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse

app = FastAPI()

# ------------------------------------------------
# http://127.0.0.1:8002/resp_json/2?q=hello
# ------------------------------------------------

@app.get("/resp_json/{item_id}", response_class=JSONResponse)
async def response_json(item_id: int, q: str | None=None):
    return {
        JSONResponse(
            content={
                "message": "hello world", 
                "item_id": item_id, 
                "q": q
            }, 
            status_code=status.HTTP_200_OK
        )
    }

# uvicorn app_05:app --port=8002 --reload