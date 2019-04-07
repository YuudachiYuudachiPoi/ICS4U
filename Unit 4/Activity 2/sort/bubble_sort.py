#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-04-07 11:52:38
LastEditTime: 2019-04-07 12:16:26
'''

def bubble_sort(nums):
  """
  This function will sort the list of numbers using bubble
  sorting. It will compare each value to the next value in
  the list; if the first is value larger, the function will
  swap their positions.
  """
  #  loop to control number of passes
  for x in range(len(nums)):
    #  loop to control number of comparisons for length of list-1
    for i in range(0,len(nums)-1):
      #  compare side-by-side elements and swap them if
      #  first element is greater than second element
      if nums[i] < nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i] #Note python allows a swap to occur in this fashion.
  return nums

#Begin mainline
nums = [22, 30, 15, 1, 7, 87, 65, 24, 22, 0]

#print out unsorted list
print ("\nUnsorted list:")
for count in nums:
    print (count, " ", end="")

nums = bubble_sort(nums)

#print out sorted list
print ("\n\nAfter sorting using the Bubble Sort, the array is: ")
for count in nums:
    print(count, " ", end="")
print()