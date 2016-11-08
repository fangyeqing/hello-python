#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '获取对象信息'
__author__ = 'fangyeqing'
__time__ = '2016/11/3'
"""

import types

# type
print(type(123))
print(type('str'))
print(type(abs))


def fn():
    pass
print(type(fn) == types.FunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type(abs)==types.BuiltinFunctionType)
print(type((x for x in range(10)))==types.GeneratorType)

# isinstance
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance('a', str))

# dir
print(dir('abc'))
print(hasattr('abc', '__init__'))
