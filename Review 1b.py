def num_input():
    try:
        num_1 = int(input('What is the number 1? '))
        num_2 = int(input('What is the number 2? '))
    except:
        print('input error')
    
    return num_1,num_2


def make_list(num_1,num_2):
    if num_1 < num_2:
        num_list = range(num_1,num_2+1)
    elif num_1 > num_2:
        num_list = range(num_1,num_2-1,-1)
    else:
        num_list = None

    return num_list

def print_list(num_list):
    try:
        string_list= []
        for num in num_list:
            string_list.append(str(num))
        message = ' '.join(string_list)
    except:
        message = 'input number is the same.'
    
    print()
    print(message)

def mian():
    not_exit = True
    while not_exit:
        num_1,num_2 = num_input()
        num_list = make_list(num_1,num_2)
        print_list(num_list)
        print()
        again = input('Would you like to try again?(Yes or yes) ').lower()
        if again != 'yes':
            not_exit = False

if __name__ == '__main__':
    mian()