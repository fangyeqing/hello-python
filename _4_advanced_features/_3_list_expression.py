#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2016/11/2'
"""


import os
# 生成[1x1, 2x2, 3x3, ..., 10x10]
print([x*x for x in range(1, 11)])
# 选出仅偶数的平方
print([x * x for x in range(1, 11) if x % 2 == 0])
# 两层循环生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
# 列出当前目录下的所有文件和目录名
print([d for d in os.listdir('.')])
# 生成表达式
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])
# list字符串变小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# test
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
