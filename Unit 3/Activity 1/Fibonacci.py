#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: use a recursive function to find the value of nth Fibonacci number
Date: 2019-03-18 12:01:09
LastEditTime: 2019-03-18 12:09:33
'''
def f(n):
    '''
    description: the main function of the program
    param {int} 
    return: int
    '''
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)

message = '''
The first Fibonacci numbers are listed as follows:
1, 1, 2, 3, 5, 8, 13, 21, 34, .....

What Fibonacci term world you like to see? '''
n = int(input(message)) #not error checking, make should you enter a int that >0
print('Element {} of the fibonacci sequence is {}'.format(n,f(n)))