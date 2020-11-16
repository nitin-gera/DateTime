# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:06:24 2018

@author: nitingera
"""

import time
import datetime

curr_time = time.asctime(time.localtime(time.time()))

print("Now it is", curr_time)

#tomorrow_time = curr_time.__add__(2)
#print(tomorrow_time)

birthday = datetime.datetime(1986, 2,4,2,0,0)

print("I was born on", birthday.isoformat(" "))