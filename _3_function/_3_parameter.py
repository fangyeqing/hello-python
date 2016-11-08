#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '函数的参数'
__author__ = 'fangyeqing'
__time__ = '2016/11/1'
"""


# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s
print(power(5))
print(power(5, 3))


# 可变参数作为默认值，指向一个地址，每次都会修改，会出错
def add_end(l=[]):
    l.append('END')
    return l
print(add_end([1, 2, 3]))
print(add_end())
print(add_end())
print(add_end())


# 将上述例子改进
def add_end1(l=None):
    if l is None:
        l = []
    l.append('END')
    return l
print(add_end1())
print(add_end1())
print(add_end1())


# 可变参数：list或者tuple传参
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc((1, 2, 3)))
print(calc([1, 2, 3]))


# 可变参数：*传参
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2, 3))


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')


# 命名关键字参数：在可变之后
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
person('Jack', 24, 3, 1, city='Beijing', job='Engineer')


# 命名关键字参数：有默认值
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person('Jack', 24, job='Engineer')


# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f2(1, 2, d=99, ext=None)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
