#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile
import re

entry = "90052"

lastNothing = entry

data = zipfile.ZipFile('channel.zip', 'r')
comments = ""

def getNothing(file_name):
  global comments
  file_name += '.txt'
  line = data.read(file_name)
  comment = data.getinfo(file_name).comment
  comments += comment
  #result = ''.join(filter(lambda s: s.isdigit(), list(line)))
  m = re.match(r'Next nothing is (\d+)', line)
  if not m:
    print line
    return None
  else:
    return m.group(1)

while lastNothing != None:
  lastNothing = getNothing(lastNothing)
  print lastNothing

print comments


