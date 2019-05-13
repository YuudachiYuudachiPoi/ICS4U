import sys,os
path = sys.path[0]
sys.path.append(path)
from lemur import *

class DesertLemur(Lemur):
    food = 'Cacti'
    colour = 'White'
    baby_death_rate = 0.66
    def __init__(self):
        Lemur.__init__(self,breed='Desert Lemur')
    def __str__(self):
        message = Lemur.__str__(self)
        message += 'Food = '+self.food+'\n'
        message += 'Colour = '+self.colour+'\n'
        message += 'Baby Death Rate = '+str(self.baby_death_rate)+'\n'
        return message