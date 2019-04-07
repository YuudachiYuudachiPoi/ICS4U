#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-04-07 11:10:16
LastEditTime: 2019-04-07 12:02:16
'''
A = [22, 30, 15, 1, 7, 87, 65, 24, 22, 0]
print(A)
n = 1
for i in range(0,len(A)):
    for j in range(len(A)-1,i,-1):
        n += 1
        if A[j] < A[j-1]:
            A[j],A[j-1] = A[j-1],A[j]
print(A)
print(n)