#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import requests
import StringIO

def filt(l):
  result = []
  temp = [0, 0]
  for item in l:
    del temp[0]
    temp.append(item)
    if temp[0] != temp[1]:
      result.append(temp[1])
  return result

url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
img = Image.open(StringIO.StringIO(requests.get(url).content))
w, h = img.size
all_items = [l[0] for l in [img.getpixel((i, h / 2)) for i in range(0, w, 7)]]
print ''.join(map(lambda c: chr(c), all_items))

level = [105, 110, 116, 101, 103, 114, 105, 116, 121]

print ''.join(map(lambda c: chr(c), level))

