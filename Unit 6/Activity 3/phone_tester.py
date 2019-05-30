#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
Date: 2019-05-26 12:13:23
LastEditors: Howie Hong(希理)
LastEditTime: 2019-05-26 12:50:59
Description: 
'''
import sys
import sys
path = sys.path[0]
sys.path.append(path)

import cell_phone
p1 = cell_phone.CellPhone(type='Iphone',speed=1.2,memory=64.0)
p1.set_carrier("Rogers")
p1.set_num_apps(10)

print(p1)