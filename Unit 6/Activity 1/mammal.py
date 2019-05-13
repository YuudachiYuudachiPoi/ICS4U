class Mammal:
    '''
    description: 
    param:
        age{int}
        weight{float}
        breed{str}
        gender{str} 
    return: 
    '''
    def __init__(self,age=None,weight=None,breed=None,gender=None):
        import random

        self.age = age
        self.weight = weight
        self.breed = breed
        self.gender = gender

        if gender == None:
            self.gender = random.choice(['Male','Female'])

    def __str__(self):
        message = self.breed+':\n'
        message += 'Age = {}\n'.format(self.age)
        message += 'Weight = {}\n'.format(self.weight)
        message += 'Gender = {}\n'.format(self.gender)
        return message