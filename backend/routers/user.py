from fastapi import APIRouter, Cookie, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from database import get_db
from models.user import User
from services.line import get_profile, get_user_id_from_cookie
from utils.logging import get_logger

import cruds.user as user_crud

router = APIRouter()
logger = get_logger()


@router.get(
    "/users/me",
    tags=["users"],
    summary="ユーザの取得",
    response_model=User,
)
async def get_user(
    user_id: str = Depends(get_user_id_from_cookie),
    db: AsyncSession = Depends(get_db),
):
    user = await user_crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get(
    "/users/me/profile",
    tags=["users"],
    summary="プロフィール情報取得",
)
def login(id_token: str = Cookie(None)):
    if id_token is None:
        raise HTTPException(status_code=401, detail="No id_token received")
    profile = get_profile(id_token)
    return profile


@router.post(
    "/users",
    tags=["users"],
    summary="新規ユーザの作成",
    response_model=User,
    status_code=201,
)
async def create_user_endpoint(
    user_id: str = Depends(get_user_id_from_cookie),
    db: AsyncSession = Depends(get_db),
):
    existing_user = await user_crud.get_user(db, user_id)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    user = User(id=user_id, thread_id="thread_default")
    return await user_crud.create_user(db, user)


@router.delete(
    "/users/me",
    tags=["users"],
    summary="ユーザの削除",
)
async def get_user(
    user_id: str = Depends(get_user_id_from_cookie),
    db: AsyncSession = Depends(get_db),
):
    user = await user_crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await user_crud.delete_user(db, user)
