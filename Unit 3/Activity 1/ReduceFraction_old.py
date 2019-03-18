#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-03-18 12:39:36
LastEditTime: 2019-03-18 19:09:54
'''
def create_prime_list(max_number): # This code is copy from Unit 2/Activity 2/eratosthenes.py
    prime_list = [2]
    for num in range(2,max_number+1):#you can change the second number to a number that greater than 2
        for divider in prime_list:
            if num%divider == 0:
                break
        else: #if the num isn't multiple of all existed dividers
            prime_list.append(num)
    return prime_list

def reduce(numerator,denominator):
    if denominator > numerator:
        prime_list = create_prime_list(numerator)
    else:
        prime_list = create_prime_list(denominator)
    
    for number in prime_list:
        if numerator%number == 0 and denominator%number == 0:
            numerator,denominator = numerator//number,denominator//number

    return numerator,denominator 

numerator = int(input('What is the numerator of your fraction? '))
denominator = int(input('What is the denominator of your fraction? '))
print()
reduced_numerator,reduced_donominstor = reduce(numerator,denominator)

print('The fraction {}/{} '.format(numerator,denominator) + 'can be reduce to {}/{}'.format(reduced_numerator,reduced_donominstor))
