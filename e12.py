#!/usr/bin/env python
# -*- coding: utf-8 -*-

import get

gfx = get.get_challenge('return/evil2.gfx')

types = ['jpg', 'png', 'gif', 'png', 'jpg']
for item in range(len(types)):
  open('evil2%d.%s' % (item, types[item]), 'wb').write(gfx[item::5])
