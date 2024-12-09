from jwt import decode, InvalidTokenError


def decode_hs256(token: str, client_id: str, client_secret: id):
    try:
        decoded_token = decode(
            jwt=token,
            key=client_secret,
            algorithms=["HS256"],
            audience=client_id
        )
        return decoded_token
    except InvalidTokenError as e:
        raise f"トークンの検証に失敗しました: {str(e)}"
