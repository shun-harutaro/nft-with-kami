from openai import AsyncOpenAI

from utils.config import get_openai_api_key

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

async def chat_summary(thread_id):
    client = get_client()
    # スレッド内のメッセージを取得
    thread_messages = await client.beta.threads.messages.list(thread_id)

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


