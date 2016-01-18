#! /usr/bin/python
# encoding: utf-8

from PIL import Image, ImageDraw, ImageFont

shougun = ['家康', '家忠', '家光', '忠輝', '義直', '頼信', '頼房']

canvas = Image.new((400, 180), (255, 255, 255))
font = ImageFont.truetype('Ricty-Regular.ttf', 30, encoding='utf-8')

draw = ImageDraw.Draw(canvas)

