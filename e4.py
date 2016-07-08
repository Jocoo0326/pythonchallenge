#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests as http
import string

host = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

def getNothing(url):
  response = http.get(url)
  if response.status_code == 200:
    text = response.text
    return fetchNothing(text)

def fetchNothing(txt):
  result = ""
  for c in txt:
    if c in string.digits:
      result += c
  return result

lastNothing = "8022"
while(lastNothing  != ""):
    url = host + lastNothing
    lastNothing = getNothing(url)
    print(lastNothing)


