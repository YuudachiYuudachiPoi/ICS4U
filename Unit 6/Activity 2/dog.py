class Dog():
    name = ''
    breed = ''
    age = 0

    def __init__(self):
        self.name = input("Input the dog's name: ")
        self.breed = input("Input the dog's breed: ")
        self.age = int(input("Input thedog's age: "))
    
    def __str__(self):
        message = '{} is a {} year old {}'.format(self.name,self.age,self.breed)
        return message