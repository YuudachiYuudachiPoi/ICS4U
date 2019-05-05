#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-05-05 16:33:18
LastEditTime: 2019-05-05 16:46:56
'''
class Dog():
    '''
    description: 
    param:
        name{str}
        breed{str}
        age{int}
        aggression{boolean}
        hunger[boolean] 
    return: 
    '''
    def __init__(self,name,breed):
        import random
        self.name = name
        self.breed = breed
        self.age = random.randint(0,25)
        self.aggression = random.choice([True,False])
        self.hunger = random.choice([True,False])

    def change_hunger_state(self,hunger):
        if isinstance(hunger,bool):
            self.hunger = hunger
    
    def change_aggression_state(self,aggression):
        if isinstance(aggression,bool):
            self.aggression = aggression

    def friendly(self,other):
        if (self.hunger or self.aggression) and (other.hunger or self.aggression):
            return False
        else:
            return True

    def __str__(self):
        message = 'Name: {}\nBreed: {}\nAge: {}\n'.format(self.name,self.breed,self.age)
        if self.aggression:
            message += 'Aggression: Yes\n'
        else:
            message += 'Aggression: No\n'
        if self.hunger:
            message += 'Hunger: Yes\n'
        else:
            message += 'Hunger: No\n'
        
        return message