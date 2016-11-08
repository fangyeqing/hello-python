#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '高阶函数'
__author__ = 'fangyeqing'
__time__ = '2016/11/2'
"""
# 变量指向函数
from functools import reduce

f = abs
print(f(-10))


# 高阶函数
def add(x, y, f1):
    return f1(x) + f1(y)
print(add(-5, 6, abs))


# map f(x)=x^2
def f(x):
	return x*x
r = map(f, range(10))
print(r)
print(list(r))
# map 转字符串
print(list(map(str, range(10))))


# reduce:实现内建函数sum
def add(x, y):
	return x + y
print(reduce(add, [1, 3, 5, 7, 9]))
L = range(10)
print(reduce(add, L[1:10:2]))
print(reduce(add, [x for x in range(1, 10) if x % 2 == 1]))


# reduce:把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
	return x*10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))


# map-reduce:实现int函数（str转int）
# map利用dict将集合str挨个转换为数字，reduce加权累加每位
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        L = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return L[s]
    return reduce(fn, map(char2num, s))
print(str2int('123'))


# test1:转换成正确的英文输出，首位大写
def normalize(name):
    l1 = name[0]
    l2 = name[1:]
    return l1.upper()+l2.lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# test2:prod求积
def prod(L):
    def multi(x, y):
        return x*y
    return reduce(multi, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# test3:字符串转浮点数
def str2float(s):
    def char2num(s):
        l = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return l[s]
    def fn1(x, y):
        return x * 10 + y
    n = s.index('.')
    s = s[:n] + s[n+1:]
    return reduce(fn1, map(char2num, s)) * pow(10, n-len(s))
print('str2float(\'123.456\') =', str2float('123.456'))


# filter:过滤偶数
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# filter：删掉空字符
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# sorted
L = [36, 5, -12, 9, -21]
print(sorted(L))
# sorted：key
print(sorted(L, key=abs))
s = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(s))
print(sorted(s, key=str.lower))
# # sorted：reverse=True逆序
print(sorted(s, key=str.lower, reverse=True))
