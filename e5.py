#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests as http
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"

data = pickle.loads(http.get(url).text)

for list in data:
  print(''.join(c[0] * c[1] for c in list))

