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
        

    def __str__(self):
        message = 'Name: {}\nBreed: {}\nAge: {}\n'.format(self.name,self.breed,self.age)
        if aggression:
            message += 'Aggression: Yes\n'
        else:
            message += 'Aggression: No\n'
        if hunger:
            message += 'Hunger: Yes\n'
        else:
            message += 'Hunger: No\n'