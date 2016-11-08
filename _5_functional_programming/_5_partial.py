#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '偏函数'
__author__ = 'fangyeqing'
__time__ = '2016/11/3'
"""
import functools

print(int('101', base=2))
# 将str转int的int函数改装成2进制
int2 = functools.partial(int, base=2)
print(int2('101'))

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))
