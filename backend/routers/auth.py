from fastapi import APIRouter
import secrets
from urllib.parse import urlencode

from fastapi.responses import RedirectResponse
from utils.config import get_line_client_id

router = APIRouter()
CLIENT_ID = get_line_client_id()


@router.get("/auth/login")
async def login():
    state = secrets.token_urlsafe(16)
#    state_store[state] = True
    base_url = "https://access.line.me/oauth2/v2.1/authorize"
    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": "http://localhost:3000/callback",
        "state": state,
        "scope": "profile openid",
    }
    redirect_url = f"{base_url}?{urlencode(params)}"
    return RedirectResponse(url=redirect_url)
