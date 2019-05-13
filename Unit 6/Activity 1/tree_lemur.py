import sys,os
path = sys.path[0]
sys.path.append(path)
from lemur import *

class TreeLemur(Lemur):

    food = 'Fruit'
    colour = 'Red'
    pack_size = 'Large groups'
    def __init__(self):
        Lemur.__init__(self,breed = 'Tree Lemur')
    
    def __str__(self):
        message = Lemur.__str__(self)
        message += 'Food = '+self.food+'\n'
        message += 'Colour = '+self.colour+'\n'
        message += 'Pack Size = '+self.pack_size+'\n'
        return message