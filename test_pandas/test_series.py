#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2017/2/21'
"""

import pandas as pd
import numpy as np


obj = pd.Series([4, 7, -5, 3])
print(obj.values, obj.index, obj, sep='\n')
# 指定索引
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2.values, obj2.index, obj2, sep='\n')

print(obj2['a'])
obj2['d'] = 6
print(obj2[['a', 'b', 'd']])
print(obj2[obj2 > 0], obj2 * 2, np.exp(obj2))
print('b' in obj2, 'e' in obj2, sep='\n')


sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)
print(pd.isnull(obj4), obj4.isnull(), sep='\n')
print(obj3 + obj4)

obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)

obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)