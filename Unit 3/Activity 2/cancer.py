#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: The program will find the number of blobs of cancerous cells in the grid.
Date: 2019-03-20 12:54:16
LastEditTime: 2019-03-20 14:16:16
'''
#grim
def write_file(file_name='./Unit 3/Activity 2/sample.txt'): #You need to change the path to make sure to work
    '''
    description: write cancer file and retrun a 15x15 2D list
    param file_name{str} #make sure you include file extension 
    return: data{list} # 15x15 2D list will '+','-' and ' '.
    '''
    file = open(file_name,'r')
    data = file.readlines()

    for n,row in enumerate(data):
        data[n] = list(row[:-1])
    file.close

    return data


if __name__ == "__main__":
    data = write_file()
    print(data)
    input()