from fastapi import FastAPI
from routes import item, user

app = FastAPI()

# router 등록
app.include_router(item.router)
app.include_router(user.router)






