from contextlib import asynccontextmanager
from fastapi import FastAPI
from utils.config import check_env_variables


@asynccontextmanager
async def lifespan(app: FastAPI):
    check_env_variables()
    yield
    print("Shutting down...")


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}
