'''
name: morse_code

This program is writen by 希理(Howie Hong)

date: 2019/2/19

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
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    codes = """.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-..
    -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..
    .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"""

    char_to_code = dict(zip(chars.lower(),codes.split()))
    code_to_char = dict(zip(codes.split(),chars.lower()))

    print('This program will encrypt or decrypt a phrase using the simple encryption method of rotating the letters')
    phrase = input('Please enter a phrase: ').upper()
    choose = input_choose()

def encrypt_or_decrypt(phrase,)
    

if __name__ == "__main__":
    main()