#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
Date: 2019-05-17 14:06:03
LastEditors: Howie Hong(希理)
LastEditTime: 2019-05-17 16:59:14
Description: 
'''

import sys
path = sys.path[0]
sys.path.append(path)
import dog

class AnimalShelter():
    dogs = []

    def __init__(self,num_of_dogs):
        '''
        description: 
        param {int} 
        return: 
        '''
        for n in range(num_of_dogs):
            try:
                self.dogs.append(dog.Dog())
            except:
                print('error: Can not add this dog')
            else:
                print('Successfully added a dog.')
    
    def add_a_dog(self):
        print()
        self.dogs.append(dog.Dog())
    
    def remove_a_dog(self):
        self.display_dogs()
        print()
        try:
            number_of_the_dog = int(input('Type the number of the dog you wish to remove. '))
        except:
            print('Can not remove this dog')
        else:
            del self.dogs[number_of_the_dog-1]
            print('who is no longer in the shelter thanks to an adoptive family.')

    def display_dogs(self):
        print()
        print('The animal shelter contains:')
        for n,dog in enumerate(self.dogs):
            print('Dog #{}:'.format(n+1),dog)
    
    def display_shelter_costs(self):
        print('\nUnder current shelter load, shelter costs are as follows:')
        daily_cost = 15
        print('${} per day.'.format(daily_cost))
        yearly_cost = daily_cost *365
        monthly_cost = yearly_cost/12
        print('${:.2f} per month on average.'.format(monthly_cost))
        print('${:.2f} per year.'.format(yearly_cost))
