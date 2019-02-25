'''
name: resistor

This program is writen by 希理(Howie Hong)

date: 2019/2/25

purpose: take three colours,separated by hyphens, and prints the value of the resistor

libary require: None
'''

colours_dir = {
    'black':0,
    'brown':1,
    'red':2,
    'orange':3,
    'yellow':4,
    'green':5,
    'blue':6,
    'violet':7,
    'grey':8,
    'white':9,
}

message = '''
What is your resitors colour code?
Separate each colur by hyphens.
Example: Red-Orange-Black
'''

colours = input(message).lower().split('-')
print()

value = ( 10*colours_dir[colours[0]]+colours_dir[colours[1]] ) * (10**colours_dir[colours[2]])
print('The value of the resistor is:',value,'ohms')