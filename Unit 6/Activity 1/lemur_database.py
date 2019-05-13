#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-05-13 11:36:33
LastEditTime: 2019-05-13 14:16:21
'''
import sys,os
path = sys.path[0]
sys.path.append(path)
from desert_lemur import *
from jungle_lemur import *
from tree_lemur import *


len_of_list = ''
while not len_of_list.isdigit():
    len_of_list = input('How many Lemurs do you want to add to the list? ')
else:
    len_of_list = int(len_of_list)

lemurs_list = []
for number_of_lemurs in range(len_of_list):

    choice = ''
    while not choice in ('1','2','3'):
        choice = input('''
            Please enter the type of Lemur to add: 
                1 - Tree Lemur
                2 - Desert Lemur
                3 - Jungle Lemur
                ''')
    else:
        choice = int(choice)

    if choice == 1:
        lemurs_list.append(TreeLemur())
        print('Creating Tree Lemur')
    elif choice == 2:
        lemurs_list.append(DesertLemur())
        print('Creating Desert Lemur')
    elif choice == 3:
        lemurs_list.append(JungleLemur())
        print('Creating Jungel Lemur')

print('Displaying the list of Lemurs:')
print('-'*20)
print('\n')
for lemur in lemurs_list:
    print(lemur)
