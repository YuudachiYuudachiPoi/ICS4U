#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-04-07 12:44:35
LastEditTime: 2019-04-07 16:07:24
'''

class NumbersList:

    def __init__(self,number_of_numbers):
        self.number_of_numbers = number_of_numbers
        #self.data = data

    def make_list(self):
        import random
        self.data = []
        for n in range(self.number_of_numbers):
            self.data.append(random.randint(0,1000))


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

    type_of_sort = 0
    while not type_of_sort in range(1,5):
        type_of_sort = int(input('''
        What type of sort would you like to perfrom?
        1 - Selection Sort
        2 - Bubble Sort
        3 - Insertion Sort
        4 - Quick Sort
        '''))
    print()

    type_of_order = 0
    while not type_of_order in range(1,3):
        type_of_order = int(input('''
        In what order do you want the numbers sorted?
        1 - Ascending
        2 - Descending
        '''))
    '''
    description: 
    param {type} 
    return: 
    '''
    print()
    
    print('The unsorted list is:')
    number_list.print()
    print('-'*30)
    message = ['Parfoming']
    if type_of_sort == 1:
        number_list.selection_sort()
        message.append('Selection Sort')
    elif type_of_sort == 2:
        number_list.bubble_sort()
        message.append('Bubble Sort')
    elif type_of_sort == 3:
        number_list.insertion_sort()
        message.append('Insertion Sort')
    elif type_of_sort == 4:
        number_list.quick_sort()
        message.append('Quick Sort')
    
    if type_of_order == 1:
        message.insert(1,'Ascending')
    elif type_of_order == 2:
        number_list.reverse()
        message.insert(1,'Descending')    

    print(' '.join(message))
    print('The sorted list is:')
    number_list.print()

if __name__ == "__main__":
    main()

'''
a = NumbersList(10)
a.make_list()
a.prt()
a.quick_sort()
a.reverse()
a.prt()
'''
