#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-04-15 17:26:50
LastEditTime: 2019-04-15 17:26:53
'''
import time
a1=time.perf_counter()
a2=time.process_time()
c=1
for i in range(1,20000):
    c*=i
b1=time.perf_counter()
b2=time.process_time()
print(b1-a1,'s')
print(b2-a2,'s')