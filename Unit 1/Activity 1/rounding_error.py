'''
name: rounding_error

This program is writen by 希理(Howie Hong)

data: 2019/2/14

purpose: This program will compares the square of the square root of any number. The difference in these values is due to the rounding error in Python.

libary require: math,sys

variable: 
    num,root,answer,error
'''

import math,sys
try:
    num = float(input('Please enter a number: '))
except:
    print('Please input a real.')
root = math.sqrt(num)
print('The square root of your number is:',root)
answer = root**2
print(root,'squared is:',answer)
error = num-answer
print('The round off error is:',error)