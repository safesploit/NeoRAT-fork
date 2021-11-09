import numpy

from PIL import Image, ImageDraw, ImageFont


def text_to_ascii(text):
  myfont = ImageFont.truetype('arial.ttf', 18)
  size = myfont.getsize(text)
  img = Image.new('1', size, 'black')
  draw = ImageDraw.Draw(img)
  draw.text((0, 0), text, 'white', font=myfont)
  pixels = numpy.array(img, dtype=numpy.uint8)
  chars = numpy.array([' ', '%'], dtype='U1')[pixels]
  strings = [line for line in chars.view('U' + str(chars.shape[1])).flatten() if not line.isspace()]
  result = '\n'.join(strings)
  
  return result