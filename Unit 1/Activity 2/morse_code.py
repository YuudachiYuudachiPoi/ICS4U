'''
name: morse_code

This program is writen by 希理(Howie Hong)

date: 2019/2/20

purpose: This program will encrypt or decrypt a phrase using the morse code

libary require: None
'''

def input_choose():
    '''
    variable require: None(type)

    function require: None

    purpose: this function will input choose

    return variable: choose(int)
    '''

    try:
        print('1 - Encryption')
        print('2 - Decryption')
        choose = int(input('Please choose 1 or 2: '))
        if not choose in range(1,3):
            choose = input_choose()
    except:
        choose = input_choose()

    return choose

def main():
    '''
    variable require: None(type)

    function require:
        input_choose
        encrypt_or_decrypt
        main

    purpose: this is the main function of the problem

    return variable: None
    '''

    print('This program will encrypt or decrypt a phrase using the simple encryption method of rotating the letters')
    phrase = input('Please enter a phrase: ').lower()
    choose = input_choose()
    try:
        encrypt_or_decrypt(phrase,choose)
    except:
        print()
        print('error: make sure you enter the right code/word and choose the right option')
        print('If there is any pronlem, please contact me')
        print()
        main()

def encrypt_or_decrypt(phrase,choose):
    '''
    variable require: 
        phrase(str,only letter or only '.'and'-')
        choose(int, 1 or 2 )# choose==1 : encrypt


    function require: None

    purpose: this function will encrypt or decrypt morse cide

    return variable: None
    '''

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    codes = """.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-..
    -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..
    .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"""

    char_to_code = dict(zip(chars.lower(),codes.split()))
    code_to_char = dict(zip(codes.split(),chars.lower()))

    if choose == 1:
        code_list = []
        print('The original phrase is:',phrase)
        for letter in phrase:
            print(char_to_code[letter])
            code_list.append(char_to_code[letter])
        print()
        print('The encrypted phrase is:',end=' ')
        for code in code_list:
            print(code,end=' ')
    elif choose == 2:
        letter_list = []
        print('The encrypted code is:',phrase)
        for letter in phrase.split(' '):
            print(code_to_char[letter])
            letter_list.append(code_to_char[letter])
        print()
        print('The decrypted letters is',end=' ')
        for letter in letter_list:
            print(letter,end='')

    

if __name__ == "__main__":
    main()