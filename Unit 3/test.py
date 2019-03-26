#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-03-26 17:29:24
LastEditTime: 2019-03-26 17:54:30
'''
def stars(n):
    if n==1 or n==0:
        print('*')
    else:
        print('*')
        stars(n-2)

#stars(6)
def what(n):
    if n==1:
        return 0
    else:
        return what(int(n/2)) + 1

#print(what(10))

def cheers(n):
    if n == 1:
        print('Hurray')
    else:
        print('Hip',end='')
        cheers(n-1)

#cheers(3)

k = 0

def fibo(n):
    global k

    k += 1

    if n==1 or n==2:
        return k
    else:
        return fibo(n-1) + fibo(n-1)

#fibo(4)
#print(k)

def mystery(a,b):
    if b==1:
        return a
    else:
        return a + mystery(a,b-1)

#print(mystery(2,3))

def hannoi(n,a,b,c):
    global k
    
    if n>0:
        hannoi(n-1,a,c,b)
        print(a,c)
        hannoi(n-1,b,a,c)
        k += 1

#hannoi(3,'a','b','c')
#print(k)

import math

print(math.factorial(4))