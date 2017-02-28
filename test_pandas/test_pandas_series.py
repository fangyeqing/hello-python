#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2017/2/21'
"""

import pandas as pd
import numpy as np

# 不指定索引
obj = pd.Series([4, 7, -5, 3])  # 索引为0,1,2,3
print(obj.values, obj.index, obj, sep='\n')
# 指定索引
obj2 = pd.Series((4, 7, -5, 3), index=['d', 'b', 'a', 'c'])
print(obj2.values, obj2.index, obj2, sep='\n')
# 字段创建
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
states = ['California', 'Ohio', 'Oregon', 'Texas']
# Series创建
obj4 = pd.Series(sdata, index=states)
print(obj3, obj4, sep='\n')

print('--------------')

# 改：索引更改
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)
# 改：值更改
obj['Bob'] = 6
print(obj[['Bob', 'Ryan', 'hehe']])
# 删
obj.drop('Bob', inplace=True)
print(obj)
# 增
obj['hehe'] = 110
print(obj)
# 查
print(obj2['a'])
print(obj2[:2])
print(obj2[obj2 > 0], obj2 * 2, np.exp(obj2))
print('b' in obj2, 'e' in obj2, sep='\n')
print('--------------')
# 算术运算
print(pd.isnull(obj4), obj4.isnull(), sep='\n')
print(obj3 + obj4)

print('--------------')
# name
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)




