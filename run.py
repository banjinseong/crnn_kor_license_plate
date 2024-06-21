#!/usr/bin/env python3
#
# Authors:
#   5jx2oh@gmail.com
# Reference:
#   https://scorchingnraining.tistory.com/31


import os
import random
import time
import argparse

from tqdm import tqdm
from PIL import Image, ImageDraw, ImageFont

# Hangul Classification Used for Vehicle License Plates
korean = '가나다라마거너더러머버서어저고노도로모보소오조구누두루무부수우주바사아자하허호배'

#
new_img_path = './number_plate_new.png'
old_img_path = './number_plate_old.png'
new_elc_img_path = './elc_plate_new.png'
old_elc_img_path = './elc_plate_old.png'

# User default path through environment variables
user_profile = os.environ['USERPROFILE']

# Hangul font download path
# https://www.juso.go.kr/notice/NoticeBoardDetail.do?mgtSn=44&currentPage=11&searchType=&keyword=
ko_font = ImageFont.truetype(f'{user_profile}/AppData/Local/Microsoft/Windows/Fonts/한길체.ttf',
                             90, encoding='unic')
# Numeric font information
# https://fonts.google.com/noto/specimen/Noto+Sans+KR
font = ImageFont.truetype(f'{user_profile}/AppData/Local/Microsoft/Windows/Fonts/NotoSansKR-Medium.ttf',
                          100, encoding='unic')


def run():
    count, save_path = opt.count, opt.save_path

    start = time.time()

    # Make folder to saving outputs
    os.makedirs(f'{save_path}/new8', exist_ok=True)
    os.makedirs(f'{save_path}/new7', exist_ok=True)
    os.makedirs(f'{save_path}/old8', exist_ok=True)
    os.makedirs(f'{save_path}/old7', exist_ok=True)
    os.makedirs(f'{save_path}/new_elc8', exist_ok=True)
    os.makedirs(f'{save_path}/new_elc7', exist_ok=True)
    os.makedirs(f'{save_path}/old_elc8', exist_ok=True)
    os.makedirs(f'{save_path}/old_elc7', exist_ok=True)


    for i in tqdm(range(count), desc='8-digit license plate(elc)'):
        front = f'{random.randint(100, 999)}'
        middle = random.choice(korean)
        back = f' {random.randint(1000, 9999)}'
        full_name = front + middle + back

        image_pil = Image.open(new_elc_img_path)
        draw = ImageDraw.Draw(image_pil)
        # draw.text( (x,y), License plate string, Font color, Font )
        draw.text((100, 0), front, 'black', font)
        draw.text((280, 45), middle, 'black', ko_font)
        draw.text((365, 0), back, 'black', font)

        image_pil.save(f'{save_path}/new_elc8/' + full_name + '.png', 'PNG')

    for i in tqdm(range(count), desc='7-digit license plate(elc)'):
        front = f'{random.randint(10, 99)}'
        middle = random.choice(korean)
        back = f' {random.randint(1000, 9999)}'
        full_name = front + middle + back

        image_pil = Image.open(new_elc_img_path)
        draw = ImageDraw.Draw(image_pil)
        draw.text((115, 0), front, 'black', font)
        draw.text((225, 45), middle, 'black', ko_font)
        draw.text((335, 0), back, 'black', font)

        image_pil.save(f'{save_path}/new_elc7/' + full_name + '.png', 'PNG') 







    for i in tqdm(range(count), desc='8-digit license plate(elc)'):
        front = f'{random.randint(100, 999)}'
        middle = random.choice(korean)
        back = f' {random.randint(1000, 9999)}'
        full_name = front + middle + back

        image_pil = Image.open(old_elc_img_path)
        draw = ImageDraw.Draw(image_pil)
        # draw.text( (x,y), License plate string, Font color, Font )
        draw.text((80, 0), front, 'black', font)
        draw.text((260, 40), middle, 'black', ko_font)
        draw.text((365, 0), back, 'black', font)

        image_pil.save(f'{save_path}/old_elc8/' + full_name + '.png', 'PNG')

    for i in tqdm(range(count), desc='7-digit license plate(elc)'):
        front = f'{random.randint(10, 99)}'
        middle = random.choice(korean)
        back = f' {random.randint(1000, 9999)}'
        full_name = front + middle + back

        image_pil = Image.open(old_elc_img_path)
        draw = ImageDraw.Draw(image_pil)
        draw.text((90, 0), front, 'black', font)
        draw.text((230, 40), middle, 'black', ko_font)
        draw.text((355, 0), back, 'black', font)

        image_pil.save(f'{save_path}/old_elc7/' + full_name + '.png', 'PNG') 













    # 8-digit license plate with holographic
    for i in tqdm(range(count), desc='8-digit license plate(holographic)'):
        front = f'{random.randint(100, 999)}'
        middle = random.choice(korean)
        back = f' {random.randint(1000, 9999)}'
        full_name = front + middle + back

        image_pil = Image.open(new_img_path)
        draw = ImageDraw.Draw(image_pil)
        # draw.text( (x,y), License plate string, Font color, Font )
        draw.text((95, -5), front, 'black', font)
        draw.text((280, 40), middle, 'black', ko_font)
        draw.text((375, -5), back, 'black', font)

        image_pil.save(f'{save_path}/new8/' + full_name + '.png', 'PNG')

    for i in tqdm(range(count), desc='7-digit license plate(holographic)'):
        front = f'{random.randint(10, 99)}'
        middle = random.choice(korean)
        back = f' {random.randint(1000, 9999)}'
        full_name = front + middle + back

        image_pil = Image.open(new_img_path)
        draw = ImageDraw.Draw(image_pil)
        draw.text((115, -5), front, 'black', font)
        draw.text((240, 40), middle, 'black', ko_font)
        draw.text((355, -5), back, 'black', font)

        image_pil.save(f'{save_path}/new7/' + full_name + '.png', 'PNG')    








    # 8-digit license plate
    for i in tqdm(range(count), desc='8-digit license plate'):
        front = f'{random.randint(100, 999)}'
        middle = random.choice(korean)
        back = f' {random.randint(1000, 9999)}'
        full_name = front + middle + back

        image_pil = Image.open(old_img_path)
        draw = ImageDraw.Draw(image_pil)
        draw.text((60, -5), front, 'black', font)
        draw.text((245, 35), middle, 'black', ko_font)
        draw.text((360, -5), back, 'black', font)

        image_pil.save(f'{save_path}/old8/' + full_name + '.png', 'PNG')

    # 7-digit license plate
    for i in tqdm(range(count), desc='7-digit license plate'):
        front = f'{random.randint(10, 99)}'
        middle = random.choice(korean)
        back = f' {random.randint(1000, 9999)}'
        full_name = front + middle + back

        image_pil = Image.open(old_img_path)
        draw = ImageDraw.Draw(image_pil)
        draw.text((85, -5), front, 'black', font)
        draw.text((215, 35), middle, 'black', ko_font)
        draw.text((335, -5), back, 'black', font)

        image_pil.save(f'{save_path}/old7/' + full_name + '.png', 'PNG')



    print(f'Done. ({round(time.time() - start, 3)}s)')  # Spending time


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', type=int, default=1200, help='Number of image to save')
    parser.add_argument('--save-path', type=str, default='result', help='Output path')
    opt = parser.parse_args()

    run()