import sys
def num_input():
    try:
        num_1 = int(input('What is the integer 1? '))
        num_2 = int(input('What is the integer 2? '))
    except:
        print('You need to enter an integer.\n')
        num_1,num_2 = num_input()

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
    if isinstance(num_list,list):
        string_list= []
        for num in num_list:
            string_list.append(str(num))
        message = ' '.join(string_list)
    else:
        message = 'input number is the same.'
    
    print()
    print(message)

def welcome():
    name = input('What is your name? ').upper()
    print('Welcome, '+name+'.')
    return name

def write_name_to_file(name):
    name_file = open('UserNames.txt','a')
    name_file.write(name+'\n')
    name_file.close

def main():
    name = welcome()
    write_name_to_file(name)
    not_exit = True
    while not_exit:
        num_1,num_2 = num_input()
        num_list = make_list(num_1,num_2)
        print_list(num_list)
        print()
        again = input('Would you like to try again?(Yes or yes) ').lower()
        if again != 'yes':
            not_exit = False
        else:
            print()

if __name__ == '__main__':
    main()