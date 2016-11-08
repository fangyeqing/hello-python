#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '第三方模块'
__author__ = 'fangyeqing'
__time__ = '2016/11/3'
"""
from PIL import Image

im = Image.open('xiaolan.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((400, 400))
im.save('xiaolan.png', 'JPEG')