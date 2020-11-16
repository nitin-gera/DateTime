# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 14:57:42 2018

@author: nitingera
"""

import time
import calendar

localtime = time.asctime(time.localtime(time.time()))

print(localtime)

month_cal = calendar.month(2018, 9)
print(month_cal)

print(time.clock())
print(time.gmtime(time.time()))

print(calendar.firstweekday())
