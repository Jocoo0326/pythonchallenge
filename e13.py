#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpclib

url = 'http://www.pythonchallenge.com/pc/phonebook.php'

photobook = xmlrpclib.ServerProxy(url)

print photobook.phone('Bert')

