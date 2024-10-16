

from PIL import Image, ImageDraw, ImageFont

# 画像全体に対するメッセージ描画可能エリアの比率
MAX_RATIO = 0.8

# フォント関連の定数
FONT_MAX_SIZE = 128
FONT_MIN_SIZE = 12

# WindowsやLinuxではパスが異なる
FONT_NAME = 'C:\\Windows\\Fonts\\malgun.ttf'
FONT_COLOR_WHITE = (255, 255, 255, 0)

# アウトプット関連の定数
OUTPUT_NAME = 'output.png'
OUTPUT_FORMAT = 'PNG'


def save_with_message(fp, message):
    image = Image.open(fp)
    draw = ImageDraw.Draw(image)
    # メッセージを描画できる領域のサイズ
    # タプルの要素ごとに計算する
    image_width, image_height = image.size
    message_area_width = image_width * MAX_RATIO
    message_area_height = image_height * MAX_RATIO

    # フォントサイズを決める
    for font_size in range(FONT_MAX_SIZE, FONT_MIN_SIZE - 1, -1):
        font = ImageFont.truetype(FONT_NAME, font_size)
        # Bounding box 계산
        bbox = draw.textbbox((0, 0), message, font=font)
        text_width = bbox[2] - bbox[0]  # x2 - x1
        text_height = bbox[3] - bbox[1]  # y2 - y1

        # 幅、高さともに領域内におさまる値を採用
        if text_width <= message_area_width and text_height <= message_area_height:
            # 메시지를 중앙에 배치
            x = (image_width - text_width) / 2
            y = (image_height - text_height) / 2
            draw.text((x, y), message, fill=FONT_COLOR_WHITE, font=font)
            break

    # 画像の保存
    image.save(OUTPUT_NAME, OUTPUT_FORMAT)