#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: The program will find the number of blobs of cancerous cells in the grid.
Date: 2019-03-20 12:54:16
LastEditTime: 2019-03-21 08:39:21
'''
grim = []
def read_file(file_name='./Unit 3/Activity 2/sample.txt'): #You need to change the path to make sure to work
    '''
    description: write cancer file and retrun a 15x15 2D list
    param file_name{str} #make sure you include file extension 
    return: data{list} # 15x15 2D list with '+','-' and ' '.
    '''
    global grim
    file = open(file_name,'r')
    data = file.read() #readlines is OK, but it will be a \n in the end of every element·.
    data = data.split('\n')
    for n,row in enumerate(data):
        data[n] = list(row)
    file.close

    grim = data

    return data

def flood_fill(row,col):
    '''
    description: flood_fill algorithm
    param {int}{int} 
    return: {Boolean}
        True: There are cencerour cells
        Flase: There is healthy cell
    '''
    global grim
    if row < 15 and row >=0 and\
        col < 15 and  col >= 0:

        if grim[row][col] == '-':
            grim[row][col] = ' '

            for n in range(-1,2):
                for i in range(-1,2):
                    flood_fill(row+n,col+i)
            
            return True
        else:
            return False

def print_grim():
    global grim
    for line in grim:
        for item in line:
            print(item,end='')
        print()

def main():
    global grim
    read_file()

    print('Your cancer date file looks like:\n')
    print_grim()

    number_of_cencer = 0
    for row,line in enumerate(grim):
        for col in range(len(line)):

            if flood_fill(row,col):
                number_of_cencer += 1
    
    print('Your file have {} cancer spots in it.'.format(number_of_cencer))
    print('You new grid is:\n')
    print_grim()
if __name__ == "__main__":
    main()