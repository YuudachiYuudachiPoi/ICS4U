#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-03-01 19:21:42
LastEditTime: 2019-03-01 20:49:25
'''
import random,os
word_list = 'Write program that plays game Hangman program should pick random word phrase from random category coded in list in the program It should display it on the screen in the format  where each  represents letter of the word or phrase The program should allow the user to guess a single letter The program should display the characters of the hangman after each guess The display should look like'.split()

word = random.choice(word_list).upper()
message = list('-'*len(word))


state = {
    0:'',\
    1:'''
     o
    ''',\
    2:'''
     o
    /
    ''',\
    3:'''
     o
    /|
    ''',\
    4:'''
     o
    /|\\
    ''',\
    5:'''
     o
    /|\\
     |
    ''',\
    6:'''
     o
    /|\\
     |
    /
    ''',\
    7:'''
     o
    /|\\
     |
    / \\
    ''',\
}

num = 0
while word != message:
    os.system('cls')
    print('''Category: a word in this paragraph
    Write a program that plays the game of Hangman. 
    The program should pick a random word or phrase from a random category (coded in a list in the program). 
    It should display it on the screen in the format: ----- --- where each - represents a letter of the word or phrase. 
    The program should allow the user to guess a single letter. 
    The program should display the characters of the hangman after each guess. 
    
    
    
    ''')
    print(''.join(message))
    print('Number of Guesses Remaining:',7-num)
    print(state[num])
    if num == 7 :
        print('you lost')
        break
    letter = input('\nGuess a letter:').upper()
    if len(letter) == 1:
        for i,n in enumerate(word):
            if n == letter:
                message[i] = word[i]
                break
        else:
            num += 1
    
else:
    print('you win')
