'''
name: Eratosthenes_old

This program is writen by 希理(Howie Hong)

date: 2019/2/25

purpose: it will finding prime numbers(No recommended to find many prime numbers, because this is very slow)

libary require: None

variable: num_list(list,global)
'''
def make_num_list(start=2,end=1000):
    '''
    variable require: 
        start(int,>1)
        end(int,>2)

    function require: None

    private variable: num_list

    purpose: it will convert range to list

    return variable: num_list(list,form small to large)
    '''

    num_list = list(range(start,end+1))
    return num_list

def remove_all_multiples(divider):
    '''
    variable require: divider(int,>1)

    function require: None

    purpose: remove every numbers that are multiples of the diveider in the num_list
    return variable: None(type)
    '''

    global num_list
    for num in num_list:
        if num%divider == 0 and num != divider:
            num_list.remove(num)

def find_the_next_divider(divider):
    '''
    variable require: None(type)

    function require: None

    purpose: it will find the next divider that grater than the last one in the num_list

    return variable: num(int,>2) or None(return None there are no any)
    '''
    global num_list
    for num in num_list:
        if num > divider:
            break
    else:
        return None
    
    return num

def main():
    '''
    variable require: None(type)

    function require:
        remove_all_muliples
        find_the_next_divider
        print_list_in_line_break


    private variable: None

    purpose: this is the main function of the program

    return variable: None(type)
    '''
    global num_list
    num_list=make_num_list()

    divider = 2
    while True:       
        remove_all_multiples(divider)
        divider = find_the_next_divider(divider)
        if divider == None:
            break
    print_list_in_line_break(num_list)

def print_list_in_line_break(num_list):
    '''
    variable require: num_list(list)

    function require: None

    private variable: None

    purpose: print list in line break

    return variable: None(type)
    '''
    for i,num in enumerate(num_list):
        print('{:<4d}'.format(num),end='')
        if (i+1)%7 == 0: #7 is num of num in each line,you can change it
            print()
        
if __name__ == "__main__":
    main()