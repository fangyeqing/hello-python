#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '切片'
__author__ = 'fangyeqing'
__time__ = '2016/11/2'
"""


L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 不使用切片
print([L[0], L[1], L[2]])

r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

# 切片
print(L[0:3])
print(L[1:3])
print(L[-1])
print(L[-3:-1])


L1 = list(range(100))
print(L1[1:20])
# 前十个数
print(L1[:10])
# 后十个数
print(L1[-10:])
# 前十个数，没两个取一个
print(L1[:10:2])
# 所有数，每5个取一个
print(L1[::5])
# 复制一个list
print(L1[:])

# tuple切片仍是tuple
print((0, 1, 2, 3, 4, 5)[:3])

# 切片用于字符串切割
s = 'ABCDEFG'
s1 = s[:3]
s2 = s[-4:]
print(s1, s2,)



