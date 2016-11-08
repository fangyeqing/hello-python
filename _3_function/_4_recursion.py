#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '递归函数'
__author__ = 'fangyeqing'
__time__ = '2016/11/1'
"""


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(5))
print(fact(10))
# print(fact(1000))
