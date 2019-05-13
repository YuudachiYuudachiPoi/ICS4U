#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-05-13 13:16:10
LastEditTime: 2019-05-13 14:19:32
'''
import sys,os
path = sys.path[0]
sys.path.append(path)
from lemur import *

class JungleLemur(Lemur):
    food = 'Mice, Snails, and Insects'
    colour = 'Black or Blue'
    mane = False
    pick_size = 'Small groups'

    def __init__(self):
        Lemur.__init__(self,breed='Jungle lemur')

    def __str__(self):
        message = Lemur.__str__(self)
        message += 'Food = '+self.food+'\n'
        message += 'Colour = '+self.colour+'\n'
        message += 'Pack Size = '+self.pick_size+'\n'
        return message