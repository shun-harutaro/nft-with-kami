FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libfreetype6-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libraqm-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY ./pyproject.toml . 
COPY ./uv.lock .

RUN uv sync --frozen --no-cache

ENV PATH="/app/.venv/bin:$PATH"

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
