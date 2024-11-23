from fastapi import FastAPI
from routers import location
from fastapi.middleware.cors import CORSMiddleware

#バックエンドは実行時に"http://localhost:8000"にアクセス

app = FastAPI()
app.include_router(location.router)

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

