#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '迭代器'
__author__ = 'fangyeqing'
__time__ = '2016/11/2'
"""
from collections import Iterable, Iterator

# 可迭代对象：Iterable判断
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))
# 迭代器：Iterator判断
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
# iter转化集合类型为Iterator
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))
