#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-05-05 16:33:18
LastEditTime: 2019-05-05 17:06:08
'''
import sys
path = sys.path[0]
sys.path.append(path)
import dog

print('Creating two dogs\n')

print('Creating the first dog.')
name = input('What is the name of the first dog? ')
breed = input('What is the breed of the first dog? ')
dog_a = dog.Dog(name,breed)
print()

print('Creating the second dog.')
name = input('What is the name of the second dog? ')
breed = input('What is the breed of the second dog? ')
dog_b = dog.Dog(name,breed)
print()

print('Here is the information for each dag\n')

print('The first dog:')
print(str(dog_a))

print('The second dog:')
print(str(dog_b))


def ask_a_question(message):
    while True:
        answer = input(message).lower()
        if answer == 'yes' or answer == 'y':
            return True
        if answer == 'no' or answer == 'n':
            return False
        if answer == '':
            return None

dog_a.change_aggression_state = ask_a_question('Is the first dog aggression now?(y/n)(blank is meaning no change) ')
dog_b.change_aggression_state = ask_a_question('Is the second dog aggression now?(y/n)(blank is meaning no change) ')
dog_a.change_hunger_state = ask_a_question('Is the first dog hunger now?(y/n)(blank is meaning no change) ')
dog_b.change_hunger_state = ask_a_question('Is the second dog hunger now?(y/n)(blank is meaning no change) ')

print()
message = 'Their meating will '
if dog_a.friendly(dog_b):
    message += 'be friendly'
else:
    message +=  'be not friendly'

print(message)