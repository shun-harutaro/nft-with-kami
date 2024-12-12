from fastapi import APIRouter, HTTPException

from schemas.text import TextResponse
from services.gpt import generate_text, create_new_thread_id, chat_summary

router = APIRouter()

shrine_info_assistant_id = "asst_kgJXT7sfAUzE63bTR5xaUunF"
talking_assistant_id = "asst_rcojtjjiQ0RoEeZOjEVlUrTC"
summary_text_assistant_id = "asst_LR1KFOmiE7o3sB3cNs3EwQY5"
omikuji_assistant_id = "asst_xAmc0FdDzbN6hKbtCGDApj40"


@router.post(
    "/gpt/shrine-info",
    tags=["gpt"],
    summary="ChatGPTによる神社取得",
)
async def gpt(shrine: str):
    try:
        thread_id = await create_new_thread_id()
        # 神社取得GPTにアクセス
        shrine_info: str = await generate_text(shrine, thread_id, shrine_info_assistant_id)
        # 神様GPTに神社情報を入れる
        generated_text: str = await generate_text(shrine_info, thread_id, talking_assistant_id)
        return {"text": generated_text, "thread_id": thread_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post(
    "/gpt/talking",
    tags=["gpt"],
    summary="ChatGPTとの対話",
)
async def gpt(text: str, thread_id: str):
    try:
        generated_text: str = await generate_text(text, thread_id, talking_assistant_id)
        return {"text": generated_text, "thread_id": thread_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/gpt/chat-summary",
    tags=["gpt"],
    summary="ChatGPTによる文章生成",
)
async def gpt(thread_id: str):
    try:
        summary = await chat_summary(thread_id)
        # "texts" のリストを結合して単一の文字列に変換
        summary_text_input = "\n".join(summary["texts"])
        summary_text: str = await generate_text(summary_text_input, thread_id, summary_text_assistant_id)
        return {"text": summary_text, "thread_id": thread_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post(
    "/gpt/omikuji",
    tags=["gpt"],
    summary="ChatGPTによる文章生成",
)
async def gpt(text: str, thread_id: str):
    try:
        generated_text: str = await generate_text(text, thread_id, omikuji_assistant_id)
        return {"text": generated_text, "thread_id": thread_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


