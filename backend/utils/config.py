import os
from typing import Dict


def check_env_variables():
    is_dev_mode: bool = get_is_dev_mode()
    env_vars: list[str] = [
        "IS_DEV_MODE",
        "OPENAI_API_KEY",
        "GOOGLE_MAPS_API_KEY",
        "LINE_CLIENT_ID",
        "LINE_CLIENT_SECRET",
        "LINE_REDIRECT_URI",
        "PINATA_API_KEY",
        "PINATA_SECRET_API_KEY",
        "NFT_ACCOUNT_ADDRESS",
        "NFT_PRIVATE_KEY",
        "FRONTEND_BASE_URI",
    ]
    env_vars_prod: list[str] = [
        # 本番環境のみで使う環境変数
        "DB_NAME",
        "DB_HOST",
        "DB_USERNAME",
        "DB_PASSWORD",
        "DB_CERT_PATH",
    ]
    if not is_dev_mode:
        env_vars.extend(env_vars_prod)
    missing_vars = [var for var in env_vars if os.getenv(var) is None]
    if missing_vars:
        raise EnvironmentError(
            f"Missing environment variables: {', '.join(missing_vars)}"
        )


def get_is_dev_mode() -> bool:
    is_dev_mode = os.getenv("IS_DEV_MODE")
    return int(is_dev_mode) == 1


def get_openai_api_key() -> str | None:
    return os.getenv("OPENAI_API_KEY")


def get_google_maps_api_key() -> str | None:
    return os.getenv("GOOGLE_MAPS_API_KEY")


def get_line_client_id() -> str | None:
    return os.getenv("LINE_CLIENT_ID")


def get_line_client_secret() -> str | None:
    return os.getenv("LINE_CLIENT_SECRET")


def get_line_redirect_uri() -> str | None:
    return os.getenv("LINE_REDIRECT_URI")


def get_pinata_api_key() -> str | None:
    return os.getenv("PINATA_API_KEY")


def get_pinata_secret_api_key() -> str | None:
    return os.getenv("PINATA_SECRET_API_KEY")


def get_nft_acount_address() -> str | None:
    return os.getenv("NFT_ACCOUNT_ADDRESS")


def get_nft_private_key() -> str | None:
    return os.getenv("NFT_PRIVATE_KEY")


def get_frontend_base_uri() -> str | None:
    return os.getenv("FRONTEND_BASE_URI")


def get_db_object() -> Dict[str, str]:
    obj = {
        "username": os.getenv("DB_USERNAME"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "database": os.getenv("DB_NAME"),
    }
    return obj


def get_db_cert_path():
    return os.getenv("DB_CERT_PATH")
