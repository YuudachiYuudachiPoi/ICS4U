'''
name: palindrome1

This program is writen by 希理(Howie Hong)

date: 2019/2/16

purpose: This program determines if a word is a palindrome

libary require: None

variable: word,word_reversed
'''

print('Words that are arranged the same way forwards as they are backwards are called palindromes.')
print('This program determines if a word is a palindrome.')

word = input('Please enter a word: ')
word_reversed = word[::-1]
print(word,'in reverse is',word_reversed)

if word.lower() == word_reversed.lower():
    print('It is a palindrome')
else:
    print('It is not a palindrome')