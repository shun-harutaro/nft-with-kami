import os


def check_env_variables():
    env_vars: list[str] = ["OPENAI_API_KEY", "OPENAI_ASSISTANT_ID", "OPENAI_THREAD_ID"]
    missing_vars = [var for var in env_vars if os.getenv(var) is None]
    if missing_vars:
        print(f"WARN Missing environment variables: {', '.join(missing_vars)}")


def get_openai_api_key() -> str | None:
    return os.getenv("OPENAI_API_KEY")


def get_openai_assistant_id() -> str | None:
    return os.getenv("OPENAI_ASSISTANT_ID")


def get_openai_thread_id() -> str | None:
    return os.getenv("OPENAI_THREAD_ID")

def get_line_client_id() -> str | None:
    return os.getenv("LINE_CLIENT_ID")

def get_line_client_secret() -> str | None:
    return os.getenv("LINE_CLIENT_SECRET")
