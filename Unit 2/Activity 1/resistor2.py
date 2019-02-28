#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: the impoved ver. of resistor
Date: 2019-02-26 13:29:43
LastEditTime: 2019-02-26 14:14:19
'''

import sys

def main():
    '''
    description: the main function of the progarm
    param {None} 
    return: None
    '''
    

    message = '''
    What is your resitors colour code?
    Separate each colur by hyphens.(case-insensitive)
    Example: Red-Orange-Black, Re-Or-Bla, red-oran-bla
    '''
    colour_list = input(message).lower().split('-')
    number_list = get_numbers(colour_list)
    
    print()

    value = ( 10*number_list[0]+number_list[1] ) * (10**number_list[2])
    print('The value of the resistor is:',value,'ohms')

def get_numbers(colour_list):
    '''
    description: input the colours and convart them to number()
    param colour_list{list,len = 3} 
    return: 
    '''
    colours_dir = {
        'black':0,
        'brown':1,
        'red':2,
        'orange':3,
        'yellow':4,
        'green':5,
        'blue':6,
        'violet':7,
        'grey':8,
        'white':9,
    }

    
    number_list = []

    if len(colour_list) == 3:
        for colour in colour_list:
            try:
                number_list.append(colours_dir[colour])
            except:
                n = 0
                for full_colour_name in colours_dir:
                    if full_colour_name.find(colour) == 0:
                        number_list.append(colours_dir[full_colour_name])
                        n += 1
                if n != 1:
                    print()
                    print('Can not recognized you input')
                    main()
                    sys.exit()

    else:
        print()
        print('Can not recognized you input')
        main()
        sys.exit()

    if len(number_list) == 3:
        return number_list
    else:
        print()
        print('Can not recognized you input')
        main()
        sys.exit()
        


if __name__ == "__main__":
    main()