from fastapi import APIRouter, Request, Response
import secrets
from urllib.parse import urlencode

from fastapi.exceptions import HTTPException
from fastapi.responses import RedirectResponse
from utils.config import get_line_client_id, get_line_redirect_uri, get_frontend_base_uri
from services.line import get_token

router = APIRouter()
CLIENT_ID = get_line_client_id()
REDIRECT_URI = get_line_redirect_uri()
FRONTEND_BASE_URI = get_frontend_base_uri()


@router.get("/auth/login")
async def login():
    state = secrets.token_urlsafe(16)
    base_url = "https://access.line.me/oauth2/v2.1/authorize"
    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "state": state,
        "scope": "profile openid",
    }
    redirect_url = f"{base_url}?{urlencode(params)}"
    response = RedirectResponse(url=redirect_url)
    response.set_cookie(
        key="auth_state",
        value=state,
        httponly=True,  # JavaScriptからアクセスさせない
        secure=True,    # httpsでのみ送信
        samesite="lax",
    )
    return response


@router.get("/auth/callback")
async def auth_callback(
    request: Request,
    code: str, state: str
    ):
    cookie_state = request.cookies.get("auth_state")
    # state検証
    if not cookie_state or cookie_state != state:
        raise HTTPException(status_code=400, detail="Invalid state parameter.")
    if not code:
        raise HTTPException(status_code=400, detail="Authorization code not found.")
    token_response = await get_token(code)

    id_token = token_response.get("id_token")
    if not id_token:
        raise HTTPException(status_code=400, detail="ID token not found.")

    response = RedirectResponse(url=FRONTEND_BASE_URI)
    response.set_cookie(
        key="id_token",
        value=id_token,
        httponly=True,
        secure=True, # httpsでのみ
        samesite="none", # クロスオリジン対応
    )
    return response
