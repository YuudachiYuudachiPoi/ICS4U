#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Howie Hong(希理)
@LastEditors: Howie Hong(希理)
@Description: 
@Date: 2019-02-28 15:48:53
@LastEditTime: 2019-03-01 14:40:27
'''
'''
test1 = [21,23,22,20,23,18,19,15,24]
test2 = [32,31,30,34,20,13,29,26,33]
test3 = [13,10,13,10,13,14,15,11,10]

results =[test1,test2,test3]

print(results[-1])
'''
def input_location(num):
    '''
    @description: input locations
    @param {int} 
    @return: list{int,int}
    '''
    try:
        location = input('choice your No.{} location ("row_col")  '.format(num)).split('_')
        location[0] = int(location[0])
        location[1] = int(location[1])
    except:
        location = input_location(num)

    if len(location) == 2 and\
        location[0]<9 and\
        location[1]<9 and\
        location[0]>0 and\
        location[1]>0:
        
        return location
    else:
        location = input_location(num)
        return location

def print_board(board):
    '''
    @description: print board
    @param {list} 
    @return: None
    '''    
    for n,row in enumerate(board):
        for i in row:
            print(i,end='')
        print()

board = []
for n in range(8):
    board.append([])
    for i in range(8):
        board[n].append(0)

print_board(board)

for n in range(8):
    location = input_location(n+1)
    board[location[0]-1][location[1]-1] = 1

print_board(board)