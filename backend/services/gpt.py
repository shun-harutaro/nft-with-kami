from openai import AsyncOpenAI

from utils.config import get_openai_api_key

import json

client = None
API_KEY = get_openai_api_key()


def get_client() -> AsyncOpenAI:
    global client
    if client is None:
        if not API_KEY:
            raise RuntimeError("API_KEYが設定されていません")
        AsyncOpenAI.api_key = API_KEY
        client = AsyncOpenAI()
    return client


async def create_new_thread_id() -> str:
    client = get_client()
    thread = await client.beta.threads.create()
    return thread.id


async def delete_thread_id(thread_id: str):
    client = get_client()
    await client.beta.threads.delete(thread_id)


async def generate_text(prompt: str, thread_id: str, assistant_id: str) -> str:
    client = get_client()
    await client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=prompt,
    )

    run = await client.beta.threads.runs.create_and_poll(
        thread_id=thread_id,
        assistant_id = assistant_id,
    )

    messages = await client.beta.threads.messages.list(
        thread_id=thread_id, run_id=run.id
    )
    message_content = messages.data[0].content[0].text
    annotations = message_content.annotations
    citations = []

    for index, annotation in enumerate(annotations):
        message_content.value = message_content.value.replace(
            annotation.text, f"[{index}]"
        )

        if file_citation := getattr(annotation, "file_citation", None):
            cited_file = client.files.retrieve(file_citation.file_id)
            citations.append(f"[{index}] {cited_file.filename}")

    return message_content.value


def contains_omikuji_phrase(text):
    # 特定のフレーズを定義
    # target_phrase = "おみくじをつくってやるからちょっと待つんじゃ。"
    target_phrase = "ちょっと待つんじゃ。"
    
    # フレーズが含まれているかを判定
    if target_phrase in text:
        return 1  # フレーズが見つかった場合
    return 0  # フレーズが見つからなかった場合



async def chat_summary(thread_id):
    client = get_client()
    # スレッド内のメッセージを取得
    thread_messages = await client.beta.threads.messages.list(thread_id, limit = 100)

    thread_messages.data.reverse()

    # "role" が "user" のメッセージのみをフィルタリング
    user_messages = [message for message in thread_messages.data if message.role == "user"]

    # "content" のテキストを抽出
    texts = [
        message.content[0].text.value
        for message in user_messages
        if message.content and message.content[0].type == "text"
    ]

    # JSON形式で返却
    return {"texts": texts}

async def get_shrineName_inthread(thread_id):
    client = get_client()

    # スレッド内の全てのメッセージを取得
    response = await client.beta.threads.messages.list(thread_id, limit = 100)

    # レスポンスの確認
    if not response or not response.data:
        return {"text": None}  # メッセージが取得できない場合

    # メッセージを時系列順に並べ替え
    thread_messages = response.data[::-1]

    # 最初の "role" が "user" のメッセージを探す
    for message in thread_messages:
        if message.role == "user" and message.content:
            if isinstance(message.content, list) and message.content and message.content[0].type == "text":
                # "~神社" のような最初の会話内容を返す
                return message.content[0].text.value

    # 該当するメッセージが見つからない場合
    return {"text": None}


 # json形式に変換 -> 使わない
def text_to_json(text):
    lines = text.strip().split("\n")
    json_data = {
        "運勢": lines[0].strip(', '),
        "願望": lines[1].split(', ')[1].strip(),
        "健康": lines[2].split(', ')[1].strip(),
        "金運": lines[3].split(', ')[1].strip(),
        "学問": lines[4].split(', ')[1].strip(),
        "恋愛": lines[5].split(', ')[1].strip(),
        "神託": "".join(lines[6:]).strip()
    }
    return json_data
 
