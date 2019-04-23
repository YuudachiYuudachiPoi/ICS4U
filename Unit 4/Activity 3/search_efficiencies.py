#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: This is a modified version of /Unit 4/Acticity 2/sorting_rountines.py
    Now, I added linear search, binary search and counters for them
Date: 2019-04-17 13:02:57
LastEditTime: 2019-04-23 08:43:13
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



    def binary_search(self,search_number,counter = True):
        '''
        description: binary search
            Note: numbers must be sorted before
        param: 
            search_number{int} 
            counter
                true: enable counter
                False: disable counter
        return: 
            is_in{boolean}
                True: number is in the list
                Flase: number is not in the list
            
            if counter is disable:
                processing_time:
                    {float}(in second) # if counter is enable
                loop_counter, comparison_counter:
                    {int} # if counter is enable
            
        '''
        if counter:
            import time
            processing_time_start = time.perf_counter()
            loop_counter = 0
            comparison_counter = 0

        left = 0
        right = len(self.data)-1
        while True:
            if counter:
                loop_counter += 1
                comparison_counter += 1
            if left <= right:
                #print(self.data[left:right+1]) #To check is binary_search working properly

                middle = (right+left)//2
                n = self.data[middle]

                if counter:
                    comparison_counter += 1
                
                if n == search_number:
                    found = True
                    break
                elif n < search_number:
                    left = middle+1
                else:
                    right = middle-1
            else:
                found = False
                break
        else:
            found = False
        
        if counter:
            processing_time = time.perf_counter() - processing_time_start
            return  found,processing_time*1000,loop_counter,comparison_counter
        else:
            return found

    def linear_search(self,search_number,sorted_list,counter = True):
        '''
        description: linear search
        param: 
            search_number{int}
            sorted_list{boolean}
                True: search in data (self.data) #make sure sorted it before, and from smaller to bigger
                False: search in original_data (self.original)
 
            counter
                true: enable counter
                False: disable counter
        return: 
            is_in{boolean}
                True: number is in the list
                Flase: number is not in the list
            
            if counter is disable:
                processing_time:
                    {float}(in ms) # if counter is enable
                loop_counter, comparison_counter:
                    {int} # if counter is enable
        '''
        if counter:
            import time
            processing_time_start = time.perf_counter()
            loop_counter = 0
            comparison_counter = 0

        if sorted_list:
            data = self.data
        else:
            data = self.original_data

        for num in data:
            if counter:
                loop_counter += 1
                comparison_counter += 1

            if num == search_number:
                found = True
                break
            
            if sorted_list:
                if counter:
                    comparison_counter += 1
                if num > search_number:
                    found = False
                    break
            
        else:
            found = False

        if counter:
            processing_time = time.perf_counter() - processing_time_start
            return  found,processing_time*1000,loop_counter,comparison_counter
        else:
            return found

    def reverse(self):
        self.data = self.data[::-1]

    def print(self):
        for num in self.data:
            print(num,end=' ')
        print()

def main():
    number_of_numbers = int(input('How many random numbers do you wish to generate? '))
    number_list = NumbersList(number_of_numbers)
    number_list.make_list()
    print('The unsorted list is:')
    number_list.print()
    number_list.quick_sort()

    search_number = int(input('What number do you want to search for? '))

    a = number_list.linear_search(search_number,sorted_list=False)
    print('-'*20+'''
    Perfoming Linear Search (unsorted list)
    Search returned: {}
    Processing Time: {}ms
    Loop_counter: {}
    Comparison_counter: {}
    '''.format(a[0],a[1],a[2],a[3]))

    a = number_list.linear_search(search_number,sorted_list=True)
    print('-'*20+'''
    Perfoming Linear Search (sorted list)
    Search returned: {}
    Processing Time: {}ms
    Loop_counter: {}
    Comparison_counter: {}
    '''.format(a[0],a[1],a[2],a[3]))

    a = number_list.binary_search(search_number)
    print('-'*20+'''
    Perfoming Binary Search
    Search returned: {}
    Processing Time: {}ms
    Loop_counter: {}
    Comparison_counter: {}
    '''.format(a[0],a[1],a[2],a[3]))

if __name__ == "__main__":
    main()
    '''
    a = NumbersList(1000)
    a.make_list()
    a.quick_sort()
    k = a.linear_search(12,sorted_list=True)
    print(k)
    '''