#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-04-03 11:54:31
LastEditTime: 2019-04-03 12:14:39
'''

def binary_search(my_array, left,right, search_for_colour):
  #Temporary print for learning purposes
  #print("Searching array: ",end="")
  #for i in range(left,right+1):
  #  print("[" + my_array[i] + "]",end="")
    
  #print(" for " + search_for_colour)
  #end temporary print

  if left > right:
      return False

  middle = (left + right) // 2
  
  if my_array[middle] == search_for_colour:
    return True

  if search_for_colour < my_array[middle]:
    return binary_search(my_array, left, middle - 1,search_for_colour)
  else:
    return binary_search(my_array, middle + 1, right,search_for_colour)

my_sorted_array = ["black", "blue", "green","orange","peach", "purple", "red", "salmon", "tan", "yellow"]
print("Binary Search: purple " , binary_search(my_sorted_array, 0, len(my_sorted_array)-1, "purple"))

print("Binary Search: green " , binary_search(my_sorted_array, 0,len(my_sorted_array)-1, "green"))
print("Binary Search: pink " , binary_search(my_sorted_array, 0,len(my_sorted_array)-1, "pink"))