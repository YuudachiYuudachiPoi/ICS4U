#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-05-05 17:08:29
LastEditTime: 2019-05-05 17:57:16
'''

import sys
path = sys.path[0]
sys.path.append(path)
import combo_lock

def ask_three_nums():
    num1 = ''
    num2 = ''
    num3 = ''
    while not(num1.isdigit() and num2.isdigit() and num3.isdigit()):
        num1 = input('  What is the first number? ')
        num2 = input('  What is the second number? ')
        num3 = input('  What is the third number? ')
    
    return int(num1),int(num2),int(num3)

print('Creating a lock')
print('Setting the combination, please answer follow question')
num1,num2,num3 = ask_three_nums()
lock_a = combo_lock.ComboLock(num1,num2,num3)
print()

print('Trying to open the lock')
num1,num2,num3 = ask_three_nums()
if lock_a.check_numbers(num1,num2,num3):
    print('The lock is opened')
else:
    print("You can't open this lock")
print()
print()

print('Creating a lock')
print('Setting the combination, randomly assigns three numbers(1-3)')
lock_b = combo_lock.ComboLock()
print()

for n in range(3):
    print('Trying to open the lock')
    num1,num2,num3 = ask_three_nums()
    if lock_b.check_numbers(num1,num2,num3):
        print('The lock is opened')
        break
    else:
        print("You can't open this lock, you have {} chance(s) remian".format(2-n))
    print()
else:
    print('the proper combination are '+str(lock_b))

