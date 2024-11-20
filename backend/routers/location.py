#フロントエンドは/frontend/src/components
from fastapi import APIRouter

router = APIRouter()

#近くの神社を返す
@router.get("/ginja_return")
async def return_shrine():

    return {"message": "Hello, World!"}
