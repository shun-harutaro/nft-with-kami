from PIL import Image,ImageDraw, ImageFont
from tempfile import NamedTemporaryFile
import os
from datetime import datetime
import requests
import io


#縦向きの文字を追加
def add_text_to_image_vertical(img, text, position, font_path, font_size, max_length=0, text_color=(0, 0, 0)):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    x, y = position
    if(max_length != 0):
        lines = wrap_text(text, max_length)
        for line in lines:
            draw.text((x, y), line, fill=text_color, font=font,direction='ttb')
            x -= font_size * 1.2  # 行間を調整
    else:
        draw.text(position, text, fill=text_color, font=font,direction='ttb')
    return img

#横向きの文字を追加
def add_text_to_image_horizontal(img, text, position, font_path, font_size, max_length, text_color=(0, 0, 0)):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    x, y = position
    if(max_length != 0):
        lines = wrap_text(text, max_length)
        for line in lines:
            draw.text((x, y), line, fill=text_color, font=font)
            y += font_size * 1.2  # 行間を調整
    else:
        draw.text(position, text, fill=text_color, font=font)
    return img


#画像を追加
def add_image_to_image(base_img, add_img, position, size):
    resized_img = add_img.resize(size, Image.Resampling.LANCZOS)
    base_img.paste(resized_img, position, mask=resized_img)
    return base_img

#指定文字数で改行を行う
def wrap_text(text, max_length):
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]

#ファイルの削除
def remove_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)

#おみくじの生成
def generate_omikuzi(img_path, font_path, omikuzi_text, shrine_name, icon_url):
    img = Image.open(img_path).copy()
    input_text = omikuzi_text.dict()
    img = add_text_to_image_vertical(img, shrine_name, (1830, 50), font_path, 50)
    img = add_text_to_image_vertical(img, input_text["運勢"], (1630, 100), font_path, 200)
    img = add_text_to_image_vertical(img, input_text["願望"], (1430, 50), font_path, 50, 20)
    img = add_text_to_image_vertical(img, input_text["健康"], (1210, 50), font_path, 50, 20)
    img = add_text_to_image_vertical(img, input_text["金運"], (990, 50), font_path, 50, 20)
    img = add_text_to_image_vertical(img, input_text["学問"], (770, 50), font_path, 50, 20)
    img = add_text_to_image_vertical(img, input_text["恋愛"], (550, 50), font_path, 50, 20)
    img = add_text_to_image_vertical(img, input_text["神託"], (320, 50), font_path, 50, 20)
    icon = load_image_from_url(icon_url)

    width, height = icon.size
    rounded_icon = create_rounded_icon(icon, (width,height))
    
    img = add_image_to_image(img, rounded_icon, (1610,530), (245,245))
    temp_file = NamedTemporaryFile(delete=False, suffix=".png")
    img.save(temp_file.name)
    temp_file.close()

    return temp_file.name

def load_image_from_url(url: str) -> Image.Image:
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status() 
        image = Image.open(io.BytesIO(response.content))
        return image
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch image from URL: {e}")
        return None
    except Exception as e:
        print(f"Failed to process image: {e}")
        return None
    


def create_rounded_icon(icon, size):
    width, height = size
    icon = icon.resize((width, height), Image.Resampling.LANCZOS).convert("RGBA")
    mask = Image.new("L", (width, height), 0)  
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=255)  
    rounded_icon = Image.new("RGBA", (width, height), (0, 0, 0, 0))  
    rounded_icon.paste(icon, (0, 0), mask=mask)  
    return rounded_icon
