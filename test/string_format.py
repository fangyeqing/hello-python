#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2017/2/21'
"""

import json
from collections import OrderedDict

aggregations = OrderedDict()
json_str = '{{\"type\": \"approxHistogramFold\",\"name\": \"{}\",\"fieldName\": \"{}\"}}'.format(2, 3)
print(json_str)

try:
    obj = json.loads(json_str)
except Exception:
    obj = {}
print(obj)
