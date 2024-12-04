from fastapi import APIRouter, HTTPException

from schemas.text import TextResponse
from services.gpt import generate_text

router = APIRouter()


@router.post(
    "/gpt",
    tags=[],
    summary="chatGPTによる文章生成",
    response_model=TextResponse,
)
async def gpt(text: str) -> TextResponse:
    try:
        generated_text: str = await generate_text(text)
        return TextResponse(text=generated_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
