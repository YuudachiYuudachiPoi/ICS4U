#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-04-07 12:23:34
LastEditTime: 2019-04-07 12:33:11
'''
def insertion_sort(data):
  for i in range (1, len(data)): 
    insert = data[i]
    move_item = i

    while move_item > 0 and data[move_item - 1] > insert:
      data[move_item] = data[move_item - 1]
      move_item -= 1
    
    data[move_item] = insert

nums = [22, 30, 15, 1, 7, 87, 65, 24, 22, 0]

#print out unsorted list
for count in range (0, len(nums)):
  print(nums[count] , end= " ")

print("\n---------------------------------")
insertion_sort(nums)

#print out sorted list
print("After sorting using the Insertion Sort, the array is:")
for count in range (0, len(nums)):
  print(nums[count] , end= " ")