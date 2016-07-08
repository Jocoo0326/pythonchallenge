#!/usr/bin/env python
# -*- coding: utf-8 -*-
from string import maketrans

s = "www.pythonchallenge.com//pc//def//map.html"

temp = []

def isLetter(c):
  asc_A = ord('A')
  asc_Z = ord('Z')
  asc_a = ord('a')
  asc_z = ord('z')
  asc = ord(c)
  if (asc >= asc_A and asc <= asc_Z) or (asc >= asc_a and asc <= asc_z):
    return True
  else:
    return False

def translate(c):
  if not(isLetter(c)):
    return c

  asc = ord(c) + 2
  asc_a = ord('a')
  asc_z = ord('z')
  if asc > asc_z:
    asc = asc - asc_z + asc_a - 1
  return chr(asc)

for c in list(s):
  temp.append(translate(c))

#print(''.join(temp))

intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trans = maketrans(intab, outtab)

print(s.translate(trans))
