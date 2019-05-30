#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
Date: 2019-05-13 11:37:28
LastEditors: Howie Hong(希理)
LastEditTime: 2019-05-13 11:37:28
Description: 
'''
import sys,os
path = sys.path[0]
sys.path.append(path)
from lemur import *

class DesertLemur(Lemur):
    '''
    description: Desert lemur 
    param: breed{int} 
    '''
    food = 'Cacti'
    colour = 'White'
    baby_death_rate = 0.66
    def __init__(self):
        Lemur.__init__(self,breed='Desert Lemur')
    def __str__(self):
        '''
        description: return a string that describe the desert lemur
        param {type} 
        return: message
        '''
        message = Lemur.__str__(self)
        message += 'Food = '+self.food+'\n'
        message += 'Colour = '+self.colour+'\n'
        message += 'Baby Death Rate = '+str(self.baby_death_rate)+'\n'
        return message