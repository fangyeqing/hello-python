#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2017/3/8'
"""
import unittest

import mock


class Target(object):
    def apply(value):
        return value


class Target1(object):
    def apply(value, are_you_sure):
        if are_you_sure:
            return value
        else:
            return None


def method(target, value):
    return target.apply(value)


class MethodTestCase(unittest.TestCase):
    def test_method(self):
        target = mock.Mock()
        method(target, "value")
        target.apply.assert_called_with("value")

    def test_method_with_2(self):
        target1 = mock.Mock()
        method(target1, "value")
        target1.apply.assert_called_with("value")