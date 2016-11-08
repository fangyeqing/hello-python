#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '访问限制'
__author__ = 'fangyeqing'
__time__ = '2016/11/3'
"""


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.set_score(score)

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            self.__score = 0

bart = Student('Bart Simpson', -98)
bart.print_score()
