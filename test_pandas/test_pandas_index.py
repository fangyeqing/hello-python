#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2017/2/24'
"""

import pandas as pd
import numpy as np


obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj3 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
obj.index = ['a', 'b', 'c', 'd']
print(obj, obj2, obj3, sep='\n------\n')


obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj4 = obj3.reindex(range(6), method='ffill')
print(obj4)


# df
frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                     columns=['Ohio', 'Texas', 'California'])
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
frame.reindex(columns=['Texas', 'Utah', 'California'])
print(frame, frame2, sep='\n------\n')