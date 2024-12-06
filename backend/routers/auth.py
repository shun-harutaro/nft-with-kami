from fastapi import APIRouter
import secrets
from urllib.parse import urlencode

from fastapi.exceptions import HTTPException
from fastapi.responses import RedirectResponse
from utils.config import get_line_client_id
from services.line import get_profile, get_token

router = APIRouter()
CLIENT_ID = get_line_client_id()


@router.get("/auth/login")
async def login():
    state = secrets.token_urlsafe(16)
    # request.session["state"] = state
    base_url = "https://access.line.me/oauth2/v2.1/authorize"
    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": "https://localhost/api/auth/callback",
        "state": state,
        "scope": "profile openid",
    }
    redirect_url = f"{base_url}?{urlencode(params)}"
    return RedirectResponse(url=redirect_url)


@router.get("/auth/callback")
async def auth_callback(
    code: str, state: str
    ):
    # TODO stateの検証
    if not code:
        raise HTTPException(status_code=400, detail="Authorization code not found.")
    token_response = await get_token(code)

    id_token = token_response.get("id_token")
    if not id_token:
        raise HTTPException(status_code=400, detail="ID token not found.")

    response = RedirectResponse(url="/")
    response.set_cookie(
        key="id_token",
        value=id_token,
        httponly=True,
        #secure=True, # httpsでのみ
        #samesite="none", # クロスオリジン対応
        #max_age=3600,
    )
    return response
