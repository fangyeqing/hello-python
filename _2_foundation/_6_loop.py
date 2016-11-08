#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2016/11/8'
"""

# for
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# range
print(list(range(1, 5)))

# while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# break
for x in range(20):
    if x == 10:
        break
    if x % 2 == 0:
        continue
    print(x)
