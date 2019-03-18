#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description:  reduce a fraction that is input by the user.
Date: 2019-03-18 12:39:36
LastEditTime: 2019-03-18 19:12:05
'''

def gcd(n1,n2):
    '''
    description: Euclidean algorithm
    param {int}{int} 
    return: {int}
    '''
    if n2 != 0:
        return gcd(n2,n1%n2)
    else:
        return n1

numerator = int(input('What is the numerator of your fraction? '))
denominator = int(input('What is the denominator of your fraction? '))
print()

if denominator > numerator:
    n = gcd(denominator,numerator)
else:
    n = gcd(numerator,denominator)
reduced_numerator,reduced_donominstor = numerator//n,denominator//n

print('The fraction {}/{} '.format(numerator,denominator) + 'can be reduce to {}/{}'.format(reduced_numerator,reduced_donominstor))
