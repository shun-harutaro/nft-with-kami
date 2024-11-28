import requests
from fastapi import APIRouter
from utils.config import (
    get_line_client_id,
    get_line_client_secret
)

router = APIRouter()
CLIENT_ID = get_line_client_id()
CLIENT_SECRET = get_line_client_secret()

@router.post(
    "/login",
    tags=[],
)
def login(code):
    # LINE API の URL
    url = "https://api.line.me/oauth2/v2.1/token"
    # 必要なデータ（適宜置き換えてください）
    data = {
        "grant_type": "authorization_code",  # 必須パラメータ
        "client_id": CLIENT_ID,       # LINE Developers で取得
        "client_secret": CLIENT_SECRET, # 同上
        "code": code,       # 認証コード（事前に取得）
        "redirect_uri": "http://localhost:3000/callback" # LINE Developers に登録したリダイレクトURL
    }
    response = requests.post(url, data=data)

    return response.json()

@router.post(
    "/profile",
    tags=[],
)
def get_profile(id_token):
    # LINE API の IDトークン検証エンドポイント
    url = "https://api.line.me/oauth2/v2.1/verify"
    
    # リクエストのペイロード
    data = {
        "id_token": id_token,             # 取得済みのIDトークン
        "client_id": CLIENT_ID     # LINE DevelopersコンソールのチャンネルID
    }
    
    response = requests.post(url, data=data)
    return response.json()
