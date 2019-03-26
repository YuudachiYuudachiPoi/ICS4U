#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-03-21 11:59:56
LastEditTime: 2019-03-21 12:43:20
'''
#word = 'abc'

word_list = []

def word_jumble(letter_not_used,new_word=''):
    global word_list
    if len(letter_not_used) == 1:
        word_list.append(new_word+letter_not_used)
        #print(new_word+letter_not_used)
    else:
        for n,letter in enumerate(letter_not_used):
            word_jumble(letter_not_used[:n]+letter_not_used[n+1:],new_word+letter)

def eliminate():
    '''
    description: eliminate the same words
    param {type} 
    return: 
    '''
    global word_list
    new_list = []
    for word in word_list:
        if not word in new_list:
            new_list.append(word)
    word_list = new_list

def main():
    global word_list
    word = input('Please enter a word: ')
    print()
    print('By rearranging the letters in you word, "'+word+'",')
    print('I have come up with the following new "words"')
    word_jumble(word)
    eliminate() #eliminate the same word
    for word in word_list:
        print(word)
        
if __name__ == "__main__":
    #word_jumble(word)
    main()