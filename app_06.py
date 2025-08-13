from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse

app = FastAPI()

# ------------------------------------------------
# http://127.0.0.1:8002/resp_html/2?item_name=banana
# ------------------------------------------------

@app.get("/resp_html/{item_name}", response_class=HTMLResponse)
async def responcse_html(item_id: int, item_name: str | None = None):
    html_str = f'''
    <html>
    <body>
        <h2>HTML Response</h2>
        <p>item_id : {item_id}<p/>
        <p>item_name : {item_name}<p/>
    </body>
    </html>
    '''

    return {
        HTMLResponse(html_str, status_code=status.HTTP_200_OK)
    }


# uvicorn app_05:app --port=8002 --reload