#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-03-18 12:39:36
LastEditTime: 2019-03-18 17:55:32
'''
def create_prime_list(max_number): # This code is copy from Unit 2/Activity 2/eratosthenes.py
    prime_list = [2]
    for num in range(2,max_number):#you can change the second number to a number that greater than 2
        for divider in prime_list:
            if num%divider == 0:
                break
        else: #if the num isn't multiple of all existed dividers
            prime_list.append(num)
            print(num)
    return prime_list

def reduce(numerator,denominator):
    if denominator > numerator:
        prime_list = create_prime_list(denominator)
    else:
        prime_list = create_prime_list(numerator)
    
    if numerator in prime_list or denominator in prime_list:

        if denominator >= numerator and denominator % numerator == 0:
            return '1/{}'.format(denominator/numerator)
        elif numerator > denominator and numerator % denominator == 0:
            return '{}/1'.format(numerator/denominator)
        else:
            return '{}/{}'.format(numerator,denominator)
    else:
        pass
