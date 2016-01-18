#! /usr/bin/python
# encoding: utf-8

from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('/usr/share/fonts/TTF/Ricty-Regular.ttf',
                          30, encoding=('unic'))

text_canvas = Image.new('RGBA', (480, 320), (255, 255, 255))
draw = ImageDraw.Draw(text_canvas)

draw.text((10, 10), u'ほげえ', font=font, fill='#000')

text_canvas.save('hello.png', 'PNG')
