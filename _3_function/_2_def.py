#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2016/11/8'
"""
import math


def my_abs(x):
    if not isinstance(x, (int, float)):     #参数检查
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-10))


# 空函数
def nop():
    pass


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

a, b = move(100, 100, 60, math.pi / 6)
print(a, b)
r = move(100, 100, 60, math.pi / 6)
print(r)
