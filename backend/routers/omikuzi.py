from fastapi import APIRouter, BackgroundTasks,Query
from pydantic import HttpUrl
from fastapi.responses import FileResponse
from fastapi import UploadFile
from schemas.omikuzi_schema import OmikuziText
from services.omikuzi_service import generate_omikuzi,remove_file
from PIL import Image

router = APIRouter()
omikuzi_template = '/app/services/omikuzi/omikuzi_template.png'
font = '/app/services/omikuzi/玉ねぎ楷書激無料版v7改.ttf'



@router.post(
    "/omikuzi",
    tags=["omikuzi"],
    summary="テキストからおみくじの生成",
    response_model=None,
)
async def omikuzi(omikuzi_text: OmikuziText, 
                  background_tasks:BackgroundTasks,
                  shrine_name:str=Query(default='拳母神社'), 
                  icon_url:HttpUrl=Query(...)
    ):
    # おみくじ画像を生成
    generated_image_path = generate_omikuzi(img_path=omikuzi_template, font_path=font, omikuzi_text=omikuzi_text, shrine_name=shrine_name, icon_url=icon_url)

    # 送信後に一時ファイルを削除
    background_tasks.add_task(remove_file, generated_image_path)

    print(generated_image_path)
    return FileResponse(
        generated_image_path,
        media_type="image/png",
        filename="omikuzi.png",
    )
