'''
name: simple_encryption

This program is writen by 希理(Howie Hong)

date: 2019/2/19

purpose: This program will encrypt or decrypt a phrase using the simple encryption method of rotating the letters.

libary require: None

[variable: None]
'''

def input_rotation_amount():
    '''
    variable require: None(type)

    function require: None

    purpose: this function will input rotation amount

    return variable: rotaton_amount(int)
    '''
    try:
        rotation_amount = int(input('Please enter a rotation amount (1-25): '))
        if not rotation_amount in range(1,26):
            rotation_amount = input_rotation_amount()
    except:
        rotation_amount = input_rotation_amount()

    return rotation_amount

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


def make_trans_table(rotation_amount):#To enhance the speed of the program, you can hardcoded in_tab
    '''
    variable require: rotation_amount(int,1 to 25)

    function require: None

    purpose: this function will return two string. in_tab is "abcd.....yzABC.....YZ"
        out_tab is the letters relative to in_tab
        for example, if rotation_amount == 1, out_tab = "bcd.....zaBCD.....ZA"

    return variable: 
        in_tab(str)
        out_tab(str)
    '''
    in_tab = ''
    for n in range(97,123): # a-z
        in_tab += chr(n)
    for n in range(65,91): # A-Z
        in_tab += chr(n)
    
    out_tab = ''
    for n in range(97,123): #corresponing letter for a-z
        changed_n = n + rotation_amount
        if changed_n > 122:
            changed_n = (changed_n-122)+97
        elif changed_n < 97:
            changed_n = 122-(97-changed_n)
        
        out_tab += chr(changed_n)

    for n in range(65,91): #corresponing letter for A-Z
        changed_n = n + rotation_amount
        if changed_n > 90:
            changed_n = (changed_n-90)+65
        elif changed_n < 65:
            changed_n = 90-(65-changed_n)
        
        out_tab += chr(changed_n)
    
    return in_tab,out_tab

                

def main():
    '''
    variable require: 

    function require:
        input_rotation_amount
        input_choose
        make_trans_table

    purpose: this is the main function of the program

    return variable: None
    '''
    print('This program will encrypt or decrypt a phrase using the simple encryption method of rotating the letters')
    phrase = input('Please enter a phrase(Case-insensitive): ')
    rotation_amount = input_rotation_amount()
    choose = input_choose()
    if choose == 2:
        rotation_amount = -rotation_amount
    in_tab,out_tab = make_trans_table(rotation_amount)

    trantab = phrase.maketrans(in_tab, out_tab)

    print('The original phrase is:',phrase)
    if choose == 1:
        print ('The encrypted phrase is:',phrase.translate(trantab))
    elif choose == 2:
        print ('The decrypted phrase is:',phrase.translate(trantab))


if __name__ == "__main__":
    main()