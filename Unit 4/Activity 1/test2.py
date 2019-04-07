#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-04-03 12:13:11
LastEditTime: 2019-04-03 12:13:33
'''
def binary_search_iter(my_array, left, right, search_for_colour):
  found = False

  while found == False and left <= right:
    middle = (left + right) // 2
    if my_array[middle] == search_for_colour:
      found = True
    elif search_for_colour < my_array[middle]:
      right = middle - 1
    else:
      left = middle + 1

  if left > right:
    return False
  else:
    return True


my_sorted_array = ["black", "blue", "green","orange","peach", "purple", "red", "salmon", "tan", "yellow"]
print("Binary Search:black ", binary_search_iter(my_sorted_array, 0,len(my_sorted_array) - 1, "black"))
print("Binary Search:green ", binary_search_iter(my_sorted_array, 0, len(my_sorted_array) - 1, "green"))
print("Binary Search:pink ", binary_search_iter(my_sorted_array, 0, len(my_sorted_array) - 1, "pink"))