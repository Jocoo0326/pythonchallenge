#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from PIL import Image
import StringIO

url = 'http://www.pythonchallenge.com/pc/return/wire.png'
strip = Image.open(StringIO.StringIO(urllib.urlopen(url).read()))
spiral = Image.new(strip.mode, (100, 100), 0)
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y, z = -1, 0, 0
for i in range(200):
    d = dirs[i % 4]
    for j in range(100 - (i + 1) / 2):
        x += d[0]
        y += d[1]
        spiral.putpixel((x, y), strip.getpixel((z, 0)))
        z += 1

spiral.show()
