#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '生成器'
__author__ = 'fangyeqing'
__time__ = '2016/11/2'
"""

# 列表生成式[]改成 ()
g = (x * x for x in range(10))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# 直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
# print(next(g))


# 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'
fib(5)


# yield定义生成器，for循环
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib(6)
print(f)
for n in f:
    print(n)


# yield定义生成器，next循环
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# yield定义生成器返回值
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield [3]
    print('step 3')
    yield (5, 5)
o = odd()
print(next(o))
print(next(o))
print(next(o))
# print(next(o))


# 杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i-1] + L[i]  for i in range(len(L))]

n=0
for t in triangles():
    print(t)
    n += 1
    if n == 10:
        break

