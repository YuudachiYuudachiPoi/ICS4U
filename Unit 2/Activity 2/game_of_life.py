#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-03-05 13:52:26
LastEditTime: 2019-03-05 16:15:37
'''
import random,time,os,copy
#---------------------------------------
def create_cells(number_of_cells):
    '''
    description: create random cells on the grid
    param number_of_cells{int,<=20**2} 
    return: 
    '''
    for i in range(number_of_cells):
        random_cell()

def random_cell():

    global grid
    num = random.randint(0,20*20-1)
    row = num//20
    col = num%20
    
    if grid[row][col] != 'o':
        grid[row][col] = 'o'
    else:                       #if cell alive,find another one
        random_cell()

#-------------------------------------------------------------------------------

def welcome():
    '''
    description: print out welcome message and ask number of cells
    param {} 
    return: number_of_cells{int,<=20**2}
    '''
    print('Welcome to the game of life!')
    try:
        number_of_cells = int(input('Please enter how many cells you want to start the game with.\n'))
    except:
        number_of_cells = welcome()
    
    if number_of_cells > 20**2:
        number_of_cells = welcome()
    
    return number_of_cells

#-----------------------------------------------------------------------------------------------

def calcuate():
    global grid
    changed_grid = copy.deepcopy(grid)
    for i,row in enumerate(grid):
        for n,unit in enumerate(row):
            num = count_neighbours(i,n)
            if unit == 'o':
                if num == 2 or num == 3:
                    pass
                else:
                    changed_grid[i][n] = '-'
            else:
                if num == 3:
                    changed_grid[i][n] = 'o'
    grid = changed_grid

def count_neighbours(row,col):
    '''
    description: count the number of neighbours
    param row{int,<20},col{int,<20} 
    return: number_of_neighbours{int,<9}
    '''    
    number_of_neighbours = 0
    for horizontal in [-1,0,1]:
        for vertical in [-1,0,1]:
            if horizontal == 0 and vertical == 0:
                pass
            else:
                if get_state(row+horizontal,col+vertical):
                    number_of_neighbours += 1
    return number_of_neighbours

def get_state(row,col):
    '''
    description: if alive returen True
        if no alive reture False
        if out of grid reture False
    param row{int,<20},col{int,<20} 
    return: state
    '''    
    global grid
    if row >= 0 and row <20 and\
        col >= 0 and col <20 :
        
        if grid[row][col] == 'o' :
            state = True
        else:
            state = False
    else:
        state = False

    return state
#---------------------------------------------------------------------------------------------
def print_grip():
    global grid
    for i in grid:
        print(' '.join(i))

def question():
    '''
    description: 
    param {} 
    return: advance_num{int or 'exit'} 
    '''
    message = '''How many generation do you want to advance?\n(0 - exit geme)
    '''
    advance_num = input(message)
    if advance_num.lower() == 'exit':
        return 0
    try:
        advance_num = int(advance_num)
    except:
        advance_num = question()
    
    if advance_num < 0:
        advance_num = question()
    
    return advance_num

def main():
    global grid
    number_of_cells = welcome()
    grid = [['-' for i in range(20)] for i in range(20)] #create 20x20 grid
    create_cells(number_of_cells)
    generation = 0
    os.system('cls')
    print('----Generation {}'.format(generation)+'-'*10)
    print()
    print_grip()
    while True:
        print()
        advance_num = question()
        if advance_num == 0:
            break
        for i in range(advance_num):
            calcuate()
            generation += 1
            time.sleep(1) #comment this if you want to run faster
            os.system('cls')
            print('----Generation {}'.format(generation)+'-'*20)
            print()
            print_grip()

if __name__ == "__main__":
    main()
