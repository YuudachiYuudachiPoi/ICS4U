#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-05-13 11:36:52
LastEditTime: 2019-05-13 14:12:20
'''
import sys,os
path = sys.path[0]
sys.path.append(path)
from mammal import *

class Lemur(Mammal):
    location = 'Madagacar'
    classification = 'Prosimian'
    coat = 'Fur'
    dominant_role = 'Famale'
    groom_using_teeth = True

    def __init__(self,breed = 'Lemur'):
        import random
        age = random.randint(0,20)
        weight = random.uniform(1,10)
        Mammal.__init__(self,age,weight,breed)
    
    def __str__(self):
        message = Mammal.__str__(self)
        message += 'Location = '+self.location+'\n'
        message += 'Classification = '+self.classification+'\n'
        message += 'Coat = ' + self.coat+'\n'
        message += 'Dominant role = '+self.dominant_role+'\n'
        return message