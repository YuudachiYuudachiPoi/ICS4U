'''
name: palindrome3

This program is writen by 希理(Howie Hong)

date: 2019/2/16

purpose: This program determines if  a sentence is palindrome

libary require: None
'''

def main():
    '''
    variable require: None(type)

    function require: word_check

    private variable:
        sentence
        changed_sentence
        check

    purpose: this is the main function of this program

    return variable: None(type)
    '''
    print('Words that are arranged the same way forwards as they are backwards are called palindromes.')
    print('This program determines if a phrase is a palindrome.')
    sentence = input('Please enter a sentence\n(do not include puncyuation marks): ')
    changed_sentence = sentence.replace(' ','')
    print()
    
    check = word_check(changed_sentence)
    if check:
        print(sentence,'is a palindromes')
    else:
        print(sentence,'is not a palindrome.')


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