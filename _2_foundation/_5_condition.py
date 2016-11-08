#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2016/11/8'
"""

age = input('birth:')
age = int(age)                  #相当于java的Integer.parse(String)
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')