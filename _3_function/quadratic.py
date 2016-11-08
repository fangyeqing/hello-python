#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def quadratic(a, b, c):
    if a == 0:
        if b == 0:
            print('该方程退化成常数项等式，无解')
            return
        else:
            print('该方程退化成一次方程，只有一个解')
            return -c/b
    else:
        d = b**2-4*a*c
        if d < 0:
            print('该二次方程无解')
            return
        elif d == 0:
            print('该二次方程只有一个解')
            x = (-b)/(2*a)
            return x
        else:
            print('该二次方程有两个解')
            x1 = (-b+math.sqrt(d))/(2*a)
            x2 = (-b-math.sqrt(d))/(2*a)
            return x1, x2

print(quadratic(0, 0, 1))
print(quadratic(0, 1, 2))
print(quadratic(1, 1, 1))
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
