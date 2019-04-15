#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-04-07 14:19:32
LastEditTime: 2019-04-15 17:43:16
'''
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheQuickSort.html was referenced
def quick_sort(data, low, high):
  if low < high:
    split_point = partition(data, low, high)
    quick_sort(data, low, split_point - 1)
    quick_sort(data, split_point + 1, high)
    
def partition(data2, first, last): 
  pivot_value = data2[first] #pivot
  left_mark = first + 1 #index of smaller element
  right_mark = last 
  done = False
  while not done:
    while left_mark <= right_mark and data2[left_mark] >= pivot_value:
      left_mark = left_mark + 1

    while data2[right_mark] <= pivot_value and right_mark >= left_mark:
      right_mark = right_mark - 1

    if right_mark < left_mark:
      done = True
    else:
      data2[left_mark], data2[right_mark] = data2[right_mark],data2[left_mark]

  data2[first],data2[right_mark] = data2[right_mark], data2[first]
  
  return right_mark

# Begin mainline - Driver code to test above functions  
nums = []

import random
for n in range(10000):
  nums.append(random.randint(0,1000))

'''
#print out unsorted list
for count in range (0,len(nums)): 
  print(nums[count] , end = " ")
'''
import time
print("\n---------------------------------")
a1 = time.process_time()
quick_sort(nums, 0, len(nums) - 1)
print((time.process_time()-a1)*1000)

'''
#print out sorted list
print("After sorting using the Quick Sort, the array is:")
for count in range (0,len(nums)): 
  print(nums[count] , end = " ")
'''
print()
