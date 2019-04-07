#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-04-04 13:38:02
LastEditTime: 2019-04-04 14:01:24
'''
'''
def lineer_search(my_array,search_for_colour):
    for i in range(0,len(my_array)):
        print(i,end=' ')
        if search_for_colour == my_array[i]:
            
            return True
    return False

my_sorted_list = ['blue','green','orange','purple','yellow']
print(lineer_search(my_sorted_list,'pink'))
'''
def binary_search(my_array, left, right, search_for_colour):
    global c
    c += 1

    if left > right:
        return False
    middle = int((left +right)/2)
    if my_array[middle] == search_for_colour:
        return True
    if search_for_colour < my_array[middle]:
        return binary_search(my_array,left, middle -1, search_for_colour)
    else:
        return binary_search(my_array,middle+1,right,search_for_colour)


my_sorted_list = ['black','brown','green','orange','purple','yellow']
c = 0
print('pink',binary_search(my_sorted_list,0,len(my_sorted_list)-1,'pink'),' ',c)