#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import urllib
import StringIO

url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
img = Image.open(StringIO.StringIO(urllib.urlopen(url).read()))
w, h = img.size

for i in range(w):
  for j in range(h):
    if (i + j) % 2 == 1:
      img.putpixel((i, j), 0)

img.show()
