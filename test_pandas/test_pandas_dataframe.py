#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2017/2/24'
"""

import pandas as pd
import numpy as np


# 创建：numpy数组
frame = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['a', 'b', 'c', 'd'], columns=['one', 'two', 'three', 'four'])
print(frame)

# 创建：相等长度列表的字典
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = pd.DataFrame(data)
print(frame)
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop'])
print(frame2)
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'])
print(frame2)
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
print(frame2)

# 创建：嵌套字典的字典
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)
frame4 = pd.DataFrame(pop, index=[2001, 2002, 2003])
print(frame4)

# 创建：其他
pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}
print(pd.DataFrame(pdata))

print('-------增-------')
# 增
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)
print('-------删-------')
# 删
del frame2['eastern']
print(frame2.columns, frame2, sep='\n')
print(frame2.drop('one', axis=0))
print(frame2.drop(['year', 'debt'], axis=1))
print('-------改-------')
# 改
frame2['debt'] = 16.5
print(frame2)
frame2['debt'] = np.arange(5.)
print(frame2)

val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)
print(frame2.T)
print(frame2.sort_index(axis=1, ascending=True))
print(frame2.sort(columns='pop'))
print('-------查-------')
# 查
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df, df.head(), df.tail(1),
      df.index, df.columns, df.values,
      df.describe(), df.T,
      df.sort_index(axis=1, ascending=False), df.sort(columns='B'), sep='\n-------\n')

print(df['A'], df.A, sep='\n------\n')

print(df[0:3], df['20130102':'20130104'], sep='\n------\n')

# 使用标签获取横截面/选择多轴/显示标签切片, 包含两个端点,降低返回对象维度
print(df.loc[dates[0]], df.loc[:, ['A', 'B']], df.loc['20130102':'20130104', ['A', 'B']], df.loc['20130102', ['A', 'B']], sep='\n------\n')
# 获取标量值(两者等价)
print(df.loc[dates[0], 'A'], df.at[dates[0], 'A'], sep='\n------\n')
# 传递整数选择位置
print(df.iloc[3], df.iloc[3:5, 0:2], df.iloc[[1, 2, 4], [0, 2]], df.iloc[1:3, :], df.iloc[:, 1:3], sep='\n------\n')
# 显式获取一个值(两者等价)
print(df.iloc[1, 1], df.iat[1, 1], sep='\n------\n')

# 布尔索引
print(df[df.A > 0], df[df > 0], sep='\n-------\n')

df2 = df[df > 0]
print(df2.dropna(how='any'))
print(df2.fillna(value=0))
print(df2.isnull())


# apply
print(df.apply(np.cumsum))
print(df.apply(lambda x: x.max() - x.min()))


# string
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s.str.lower())


# concat
df = pd.DataFrame(np.random.randn(10, 4))
print(df[:3], df[3:7], df[7:], sep='\n-------\n')
pieces = [df[:3], df[3:7], df[7:]]
print(pd.concat(pieces))

# merge
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4'],
                     'key2': ['K0', 'K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3', 'C4'],
                      'D': ['D0', 'D1', 'D2', 'D3', 'D4']})

df3 = pd.merge(left, right, on='key', suffixes=('_left', '_right'))

df4 = pd.merge(left, right, on=['key', 'key2'])
df5 = pd.merge(left, right, on=['key', 'key2'], how='left')
df6 = pd.merge(left, right, on=['key', 'key2'], how='right')
df7 = pd.merge(left, right, on=['key', 'key2'], how='outer')

print(df3, df4, df5, df6, df7, sep='\n--------\n')


# append
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
s = df.iloc[3]
print(df.append(s, ignore_index=True))


# group by
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
print(df, df.groupby('A').sum(), df.groupby(['A', 'B']).sum(), sep='\n------\n')

# pivot table
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})
df_pivot = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], fill_value=0)
print(df, df_pivot, sep='\n-----pivot-----\n')