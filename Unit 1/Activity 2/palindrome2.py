'''
name: palindrome2

This program is writen by 希理(Howie Hong)

date: 2019/2/16

purpose: This program determines if the words in a sentence are palindrome

libary require: None
'''

def main():
    '''
    variable require: None(type)

    function require: word_check

    private variable:
        word_list
        word
        check
        palindromes_list

    purpose: this is the main function of this program

    return variable: None(type)
    '''
    print('Words that are arranged the same way forwards as they are backwards are called palindromes.')
    print('This program determines if a word is a palindrome.')
    word_list = input('Please enter a sentence\n(do not include puncyuation marks): ').split()
    print()
    
    palindromes_list = []
    for word in word_list:
        check = word_check(word)
        if check:
            palindromes_list.append(word)
    
    print('There are',len(palindromes_list),'palindromes in this sentense')
    print('The palindromes are:')
    print(', '.join(palindromes_list))


def word_check(word):
    '''
    variable require: word(str)

    function require: None

    private variable:
        word_reversed
        word
        check

    purpose: this is the main function of this program

    return variable: None(type)
    '''
    word_reversed = word[::-1]

    if word.lower() == word_reversed.lower():
        check = True
    else:
        check = False
    
    return check

if __name__ == "__main__":
    main()