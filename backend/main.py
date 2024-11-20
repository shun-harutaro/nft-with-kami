from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/kawaryo")
async def kawaryo():
    return {"message": "kawaryo"}
