#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: word pyramid
Date: 2019-03-21 12:43:37
LastEditTime: 2019-03-21 12:51:43
'''

def word_pyramid(word,n=0):
    if len(word) - 2 <= 0:
        print(' '*n + word)
        return
    else:
        print(' '*n + word)
        word_pyramid(word[1:-1],n+1)

#word = 'towering'
def main():
    word = input('Please enter a word: ')
    print("Let's build a pyramid using your word:")
    word_pyramid(word)

if __name__ == "__main__":
    main()