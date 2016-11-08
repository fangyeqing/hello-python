#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2016/11/7'
"""
# 编码
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 格式化输出
s1 = 72
s2 = 85
s3 = (s1-s2)/s1*100
print('%.2f%%' % s3)