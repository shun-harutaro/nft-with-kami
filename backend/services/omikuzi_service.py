from PIL import Image,ImageDraw, ImageFont
from tempfile import NamedTemporaryFile
import os

#縦向きの文字を追加
def add_text_to_image_vertical(img, text, position, font_path, font_size, max_length=0, text_color=(0, 0, 0)):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    x, y = position
    # 指定文字数で改行
    if max_length > 0:
        lines = wrap_text(text, max_length)
        for line in lines:
            for char in line:  # 1文字ずつ描画
                if(char == '。' or  char == '、'):
                    draw.text((x+35, y-35), char, font=font, fill=text_color)
                else:
                    draw.text((x, y), char, font=font, fill=text_color)
                y += font_size  # 文字ごとに下へ移動
            x -= font_size * 1.2  # 行間を調整
            y = position[1]  # 縦位置をリセット
    else:
        for char in text:
            draw.text((x, y), char, font=font, fill=text_color)
            y += font_size  # 文字ごとに下へ移動
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
def add_image_to_image(base_img,add_img ,position, size):
    base_img.paste(add_img.resize(size), position)
    return base_img

#指定文字数で改行を行う
def wrap_text(text, max_length):
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]

#ファイルの削除
def remove_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)

#おみくじの生成
def generate_omikuzi(img_path, font_path, omikuzi_text):
    img = Image.open(img_path).copy()
    input_text = omikuzi_text.dict()

    img = add_text_to_image_vertical(img, input_text["運勢"], (1600, 100), font_path, 250)
    img = add_text_to_image_vertical(img, input_text["願望"], (1430, 50), font_path, 50, 20)
    img = add_text_to_image_vertical(img, input_text["健康"], (1210, 50), font_path, 50, 20)
    img = add_text_to_image_vertical(img, input_text["金運"], (990, 50), font_path, 50, 20)
    img = add_text_to_image_vertical(img, input_text["学問"], (770, 50), font_path, 50, 20)
    img = add_text_to_image_vertical(img, input_text["恋愛"], (550, 50), font_path, 50, 20)
    img = add_text_to_image_vertical(img, input_text["ひとこと"], (340, 50), font_path, 50, 20)

    # 一時ファイルに保存
    temp_file = NamedTemporaryFile(delete=False, suffix=".png")
    img.save(temp_file.name)
    temp_file.close()

    return temp_file.name