#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-03-01 15:00:15
LastEditTime: 2019-03-05 16:25:36
IMPORTANT NOTE!!!!!:
    make sure you change the size of the windows to fit entire tables
    or you can make the name of schools shorter\
        and change the default number of format_number in function print_in_format
'''

import os,sys

schools = ('Catholic Central',\
    'Holy Cross',\
    'John Paul II',\
    'Mother Teresa',\
    'Regina Mundi',\
    'St. Joseph',\
    'St. Mary',\
    'St. Thomas Aquinas')

amount_options = (\
    ('25 cents',0.25),\
    ('50 cents',0.5),\
    ('1 dollar',1.0),\
    ('2 dollars',2.0))

def table_init():
    '''
    description: initialize the population_table, money_table
    param {None} 
    return: None
    '''
    global amount_options,schools,population_table,money_table

    population_table = []
    for n in range(len(amount_options)):
        population_table.append([])
        for i in range(len(schools)+1): #include Total
            population_table[n].append(0) 
    population_table.append(0) #total 

    money_table = []
    for n in range(len(amount_options)):
        money_table.append([])
        for i in range(len(schools)+1): #include Total
            money_table[n].append(0)
    money_table.append(0) #total of money
table_init()

#---------------------------------------------------------

def main():
    '''
    @description: this the main function of the program 
    @param {None} 
    @return: None
    '''
    global schools,amount_options,population_table
    
    school_choice = welcome()
    if school_choice == 8:
        table_init()
        main()
    elif school_choice == 9:
        sys.exit()
    
    else:
        amount_choice = input_amount()
        if amount_choice == 9:
            main()
        else:
            write_table(amount_choice,school_choice)
            calculate()
    
    main()


def write_table(amount_choice,school_choice):
    '''
    description: ask the population of the school and write into the population_table
    param amount_choice{int},school_choice{int} 
    return: population{int}
    '''
    global population_table,schools
    os.system('cls')
    print_table()
    try:
        population = input('What is the population of '+schools[school_choice]+'?\n(add + in front of the number if you want to add the number to the original number)(For example: +1000, 4000)\n')
        if population[0] == '+':
            population = population_table[amount_choice][school_choice] + int(population[1:])
        else:
            population = int(population)
    except:
        population = write_table(amount_choice,school_choice)

    population_table[amount_choice][school_choice] = population
    return population

def calculate():
    '''
    description: calculate by using population_table
        it will calculate 
        the total number of population,
        the money for each amount
        the total number of money
        and write it to money_table and population_table
    param {type} 
    return: 
    '''
    global population_table,money_table,amount_options

    #---------------------------------------------calculate population table
    for row,amount in enumerate(population_table[:-1]): #calculate the total population for each amount
        total = 0
        for population in amount[:-1]:
            total += population
        population_table[row][-1] = total
    
    total = 0
    for amount in population_table[:-1]: #calulate the total population for all
        total += amount[-1]
    population_table[-1] = total

    #----------------------------------------------calculate money table
    for row,amount in enumerate(population_table[:-1]):
        for col,population in enumerate(amount[:-1]):
            money_table[row][col] = population*(amount_options[row][1])
    
    for row,amount in enumerate(money_table[:-1]): #calculate the total money for each amount
        total = 0
        for money in amount[:-1]:
            total += money
        money_table[row][-1] = total
    
    total = 0
    for amount in money_table[:-1]: #calulate the total money for all
        total += amount[-1]
    money_table[-1] = total

def print_in_format(message,format_number = 20):
    print(('{:<'+str(format_number)+'}').format(message),end='')

def print_table(mode=0):
    '''
    description: print table
        mode 0: print both table
        mode 1: print population table
        mode 2: print money table
    param mode{int} 
    return: 
    '''
    global population_table,money_table,schools,amount_options

    if mode == 0:
        print_table(mode=1)
        print_table(mode=2)
    else:
        if mode == 1:
            title = 'Population Table'
            table = population_table
            all_total_message = 'TOTAL POPULATION'
        elif mode == 2:
            title = 'Money Table'
            table = money_table
            all_total_message = 'TOTAL DONATIONS'
        
        print('======================================')
        print(title+'\n')

        print_in_format('')
        for school in schools:
            print_in_format(school)
        print_in_format('TOTAL')
        print()
        
        for n,amount in enumerate(table[:-1]):
            print_in_format(amount_options[n][0]+' -')

            for element in amount:
                print_in_format(element)
            print()
        print(all_total_message+' =',table[-1])
        print('======================================\n')


def input_amount():
    '''
    description: print out message and input amount choice
        9 is Cencel
    param {type} 
    return: choice {int}
    '''
    global amount_options
    os.system('cls')
    print_table()
    print('What is the donation amount?')
    for num,option in enumerate(amount_options):
        print('{} - '.format(num)+option[0])
    print('9 - Cancel')

    try:
        choice = int(input())
        if not choice in [0,1,2,3,9]:
            choice = input_amount()
    except:
        choice = input_amount()

    return choice


def welcome():
    '''
    description: print out welcome message and input school choice
        8 is initialize all the tables
        9 is EXIT
    param {None} 
    return: choice {int}
    '''
    global schools
    os.system('cls')
    print_table()
    print('Which school is doing fundrasising?')
    for num,school in enumerate(schools):
        print('{} - '.format(num)+school)
    print('8 - Clean all the table')
    print('9 - EXIT')

    try:
        choice = int(input())
        if not choice in range(10):
            choice = welcome()
    except:
        choice = welcome()

    return choice



if __name__ == "__main__":
    main()