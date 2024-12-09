from fastapi import APIRouter, Cookie
from services.line import get_user_id, get_profile


router = APIRouter()


@router.get("/users/me")
async def login(id_token: str = Cookie(None)):
    if id_token:
        user_id = get_user_id(id_token)
        profile = get_profile(id_token)
        return { "id": user_id, **profile }
    return {"message": "No cookie received"}
