#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: A modified version of Unit 4/Activity 2/sorting_routines.py
    Now, it have counters
Date: 2019-04-07 12:44:35
LastEditTime: 2019-04-18 12:41:28
'''

class NumbersList:
    #I used copy.copy , I will not copy the elements in the list.
    #If you want to change the number in the list, please use copy.deepcopy

    #In order to keep study different methods,I didn't apply the change of the self.data
    #If you want to apply the change, you can uncomment self.data = data in all methods

    def __init__(self,number_of_numbers):
        self.number_of_numbers = number_of_numbers
        #self.data = data

    def make_list(self):
        import random
        self.data = []
        for n in range(self.number_of_numbers):
            self.data.append(random.randint(0,1000))


    def selection_sort(self):
        import copy
        data = copy.copy(self.data)

        loop_counter = 0
        comparison_counter = 0
        shift_counter = 0

        for i in range(len(data)-1):
            loop_counter += 1
            smallest = i
            for index in range(i+1,len(data)):
                loop_counter += 1
                comparison_counter +=1
                if data[index] < data[smallest]:
                    smallest = index
            shift_counter += 2
            data[i], data[smallest] = data[smallest],data[i]
        #self.data = data   #uncomment this if you want to apply changes
        return (loop_counter,comparison_counter,shift_counter)

    def bubble_sort(self):
        import copy
        data= copy.copy(self.data)

        loop_counter = 0
        comparison_counter = 0
        shift_counter = 0

        for x in range(len(data)):
            loop_counter += 1
            for i in range(len(data)-1,x,-1):
                loop_counter += 1
                comparison_counter += 1
                if data[i] < data[i - 1]:
                    shift_counter += 2
                    data[i],data[i-1] = data[i-1],data[i]
        #self.data = data   #uncomment this if you want to apply changes

        return (loop_counter,comparison_counter,shift_counter)
 
    def insertion_sort(self):
        import copy
        data = copy.copy(self.data)

        loop_counter = 0
        comparison_counter = 0
        shift_counter = 0

        for i in range (1, len(data)): 
            loop_counter += 1

            insert = data[i]
            move_item = i

            while True:
                loop_counter += 1
                comparison_counter += 1
                if move_item > 0 and data[move_item - 1] > insert:
                    loop_counter += 1
                    
                    shift_counter += 2
                    data[move_item] = data[move_item - 1]
                    move_item -= 1
                else:
                    break
                
            data[move_item] = insert
        
        return (loop_counter,comparison_counter,shift_counter)
        #self.data = data   # uncomment this if you want to apply changes
        
    def quick_sort(self,data=None,loop_counter = 0,comparison_counter = 0,shift_counter = 0):
        '''
        description: quick_sort
        param {None or list} 
        return:
            if sorting is finish 
                (loop_counter,comparison_counter,shift_counter)
            if sorting is not finish
                (data,loop_counter,comparison_counter,shift_counter)
        '''
        if data == None:
            import copy
            data = copy.copy(self.data)

        if len(data) > 1:
            first = data[0]
            left,right,mid = [],[],[first]
            for num in data[1:]:
                
                loop_counter += 1
                comparison_counter += 1
                shift_counter += 1

                if num < first:
                    left.append(num)
                elif num > first:
                    right.append(num)
                else:
                    mid.append(num)
            
            returned_tuple = self.quick_sort(left,loop_counter,comparison_counter,shift_counter)
            sorted_left = returned_tuple[0]
            loop_counter += returned_tuple[1]
            comparison_counter += returned_tuple[2]
            shift_counter += returned_tuple[3]
            
            returned_tuple = self.quick_sort(right,loop_counter,comparison_counter,shift_counter)
            sorted_right = returned_tuple[0]
            loop_counter += returned_tuple[1]
            comparison_counter += returned_tuple[2]
            shift_counter += returned_tuple[3]

            data = sorted_left + mid + sorted_right
              
            if len(data) == len(self.data):
                return (loop_counter,comparison_counter,shift_counter)
                #self.data = data   #uncomment this if you want to apply changes
            else:
                return (data,loop_counter,comparison_counter,shift_counter)
             
        else:
            return (data,loop_counter,comparison_counter,shift_counter)

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

    import time
    for type_of_sort in range(1,5):
        print('-'*30)
        if type_of_sort == 1:
            print('Parfoming Selection Sort')

            start = time.process_time() #time.clock will be removed from python 3.8
            counters = number_list.selection_sort()
            used_time = time.process_time() - start

        elif type_of_sort == 2:
            print('Parfoming Bubble Sort')

            start = time.process_time()
            counters = number_list.bubble_sort()
            used_time = time.process_time() - start

        elif type_of_sort == 3:
            print ('Parfoming Insertion Sort')

            start = time.process_time()
            counters = number_list.insertion_sort()
            used_time = time.process_time() - start

        elif type_of_sort == 4:

            print('Parfoming Quick Sort')

            start = time.process_time()
            counters = number_list.quick_sort()
            used_time = time.process_time() - start

        print('Processing time: {}ms'.format(used_time*1000))
        print('Loop counter: {}'.format(counters[0]))
        print('Comparison counter: {}'.format(counters[1]))
        print('Shift counter: {}'.format(counters[2]))
        print()



if __name__ == "__main__":
   main()

'''
    a = NumbersList(40)
    a.make_list()
    a.print()
    a.insertion_sort()
    a.print()
'''
