#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-04-07 11:21:33
LastEditTime: 2019-04-07 11:43:47
'''
def selection_sort(data):
  for i in range (0,len(data)-1):

    smallest = i
    #see if there is a smaller number further in the array
    for index in range (i+1,len(data)):
      if data[index] < data[smallest]:
        #swap values - note in many languages a swap function would need to be built
        #but python allows the exchange of data in the following method.
        data[index], data[smallest] = data[smallest],data[index]

#Begin mainline       
nums = [22, 30, 15, 1, 7, 87, 65, 24, 22, 0]

#print out unsorted list
for count in range (0,len(nums)):
  print(nums[count] , end = " ")
    
print("\n---------------------------------")
selection_sort(nums)

#print out sorted list
print("After sorting using the Selection Sort, the array is:")
for count in range (0,len(nums)):
  print(nums[count] , end = " ")