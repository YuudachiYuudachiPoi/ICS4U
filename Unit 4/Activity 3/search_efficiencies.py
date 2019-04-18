#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: This is a modified version of /Unit 4/Acticity 2/sorting_rountines.py
    Now, I added linear search, binary search and counters for them
Date: 2019-04-17 13:02:57
LastEditTime: 2019-04-17 13:05:32
'''

class NumbersList:

    def __init__(self,number_of_numbers):
        self.number_of_numbers = number_of_numbers
        #self.data = data

    def make_list(self):
        import random,copy
        self.data = []
        for n in range(self.number_of_numbers):
            self.data.append(random.randint(0,1000))
        self.original_data = copy.copy(self.data) #change it to deepcopy if you want to modify the number in the list



    def selection_sort(self):
        for i in range(len(self.data)-1):
            smallest = i
            for index in range(i+1,len(self.data)):
                if self.data[index] < self.data[smallest]:
                    self.data[index], self.data[smallest] = self.data[smallest],self.data[index]

    def bubble_sort(self):
        for x in range(len(self.data)):
            for i in range(len(self.data)-1,x,-1):
                if self.data[i] < self.data[i - 1]:
                    self.data[i],self.data[i-1] = self.data[i-1],self.data[i]
 
    def insertion_sort(self):
        for i in range (1, len(self.data)): 
            insert = self.data[i]
            move_item = i

            while move_item > 0 and self.data[move_item - 1] > insert:
                self.data[move_item] = self.data[move_item - 1]
                move_item -= 1
                
            self.data[move_item] = insert
                    
    def quick_sort(self,data=None):
        if data == None:
            data = self.data
        if len(data) > 1:
            first = data[0]
            left,right,mid = [],[],[first]
            for num in data[1:]:
                if num < first:
                    left.append(num)
                elif num > first:
                    right.append(num)
                else:
                    mid.append(num)
            
            data = self.quick_sort(left) + mid + self.quick_sort(right)
            if len(data) == len(self.data):
                self.data = data
            else:
                return data 
        else:
            return data



    def binary_seach(numbers,seach_number):
        '''
        description: binary seach
        param: 
            numbers{list} #all int
            seach_number{int} 
        return: is_in{boolean}
            True: number is in the list
            Flase: number is not in the list
        '''
        left = 0
        right = len(numbers)-1
        while left <= right:

            #print(numbers[left:right+1]) #To check is binary_seach working properly

            middle = (right+left)//2
            n = numbers[middle]
            if n == seach_number:
                found = True
                break
            elif n < seach_number:
                left = middle+1
            else:
                right = middle-1
        else:
            found = False
            
        return found

    def reverse(self):
        self.data = self.data[::-1]

    def print(self):
        for num in self.data:
            print(num,end=' ')
        print()
