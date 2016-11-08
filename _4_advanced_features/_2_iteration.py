#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '迭代'
__author__ = 'fangyeqing'
__time__ = '2016/11/2'
"""

# dict迭代
from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k, v)
# 字符串迭代
for ch in 'ABC':
    print(ch)
# 判断是否可以迭代
print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))
# 类java下标循环
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# 两个变量，list元素中为tuple
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
