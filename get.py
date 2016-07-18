#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib

def get_challenge(url):
  return urllib.urlopen('http://www.pythonchallenge.com/pc/' + url).read()
