#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-02-28 12:57:01
LastEditTime: 2019-02-28 13:02:39
'''
die1 = [1,0,2,0,3,1]
die2 = [2,1,0,4,0,3]
die3 = [3,0,3,0,3,4]
die4 = [2,0,1,0,3,5]
die5 = [1,0,2,0,3,4]
dic6 = [4,0,1,2,3,2]
dice = [die1,die2,die3,die4,die5,dic6]

t = 0
for row in range(0,len(dice)):
        t += dice[row][2]
print(t)