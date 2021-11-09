from PIL import ImageFont, Image, ImageDraw, ImageOps

from domestic.utility.write_error import *


def text_to_image(text):
	PIXEL_ON = 255
	PIXEL_OFF = 1

	grayscale = 'L'
	lines = tuple(l.rstrip() for l in text.split('\n'))

	large_font = 40
	font_path = 'cour.ttf'

	try:
		font = ImageFont.truetype(font_path, size=large_font)
	except IOError as err:
		write_error(err)
		font = ImageFont.load_default()

	pt2px = lambda pt: int(round(pt * 96.0 / 72))
	max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
	test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	max_height = pt2px(font.getsize(test_string)[1])
	max_width = pt2px(font.getsize(max_width_line)[0])
	height = max_height * len(lines)
	width = int(round(max_width + 40))
	image = Image.new(grayscale, (width, height), color=PIXEL_OFF)
	draw = ImageDraw.Draw(image)

	vertical_position = 5
	horizontal_position = 5
	line_spacing = int(round(max_height * 0.8))

	for line in lines:
		draw.text((horizontal_position, vertical_position), line, fill=PIXEL_ON, font=font)
		vertical_position += line_spacing
	c_box = ImageOps.invert(image).getbbox()
	image = image.crop(c_box)

	return image