#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-04-03 12:22:06
LastEditTime: 2019-04-03 13:09:57
'''
def read_file(file_name='./Unit 4/Activity 1/Psalms2.txt'): #You need to change the path to make sure to work
    '''
    description: read psalms file and create a list and a dir
    param: file_name{str} #make sure you include file extension 
    return: 
        numbers{list}
        number_to_title{dir}
    '''
    numbers = []
    number_to_title = {}
    file = open(file_name,'r')
    data = file.read() #readlines is OK, but it will be a \n in the end of every element·.
    data = data.split('\n')
    file.close

    for n in range(0,len(data)-1,2):
        number = int(data[n])
        numbers.append(number)

        number_to_title[number] = data[n+1]

    return numbers,number_to_title

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

numbers,number_to_title = read_file()
number = int(input('What psalm number would you like to see?(1 -99) '))
if binary_seach(numbers,number):
    print('Psalm {}'.format(number))
    print(number_to_title[11])
else:
    print('number was not found')