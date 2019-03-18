#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: calculate nCr
Date: 2019-03-18 12:12:10
LastEditTime: 2019-03-18 19:12:52
'''

def factorial(n):#you can use factorial function in math to replace it
    '''
    description: n factorial 
    param {int} 
    return: int
    '''
    if n == 1 or n == 0:
        return 1
    else:
        return n* factorial(n-1)

def c(n,r):
    '''
    description: n Choose r
    param {int}{int} 
    return: int
    '''
    return factorial(n)/(factorial(r)*factorial(n-r))

message = '''
This program will calculate the number of ways to choose
r different objects from a set of n objects
'''
print(message)

r = int(input('How many objects would you like to choose? '))#not error checking, make should you enter a int that >=0
n = int(input('How many objects are there to choose from? '))#not error checking, make should you enter a int that >=0

print('There are {} ways to choose {} objects from a set of {} objects.'.format(int(c(n,r)) ,r,n) )
