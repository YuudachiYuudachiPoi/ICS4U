'''
name: area_of_triangle

This program is writen by 希理(Howie Hong)

date: 2019/2/14

purpose: this program will calculates the area of a scalene triangle using the length of three side

libary require: Math

variable: None
'''

#Be known, I didn't a triangle checking function('6 6 6' will work in this program), becuase it need quite a lot work

def ask_length():

    '''
    variable require: None(type)

    function require: None

    private variable:
        a_b_c
        side_list

    purpose: input the length of three side

    return variable: side_list(list (all int,len = 3) )
    '''

    a_b_c = input("What is the length of three side? (please input by format 'a b c') ")
    try:
        side_list = a_b_c.split(' ')
        int_side_list = []
        for side in side_list:
            int_side_list.append(int(side))
        side_list = int_side_list
    except:
        print("Please use the right format 'a b c'.")
        side_list = ask_length()

    return side_list

def calculate(length_of_three_side):
    '''
    variable require: length_of_three_side(list (all int, len = 3) )

    function require: None

    private variable:
        a,b,c
        s,area

    purpose: calculate the area by length of three side

    return variable: area(float)

    libary require: Math
    '''

    import math 
    a = length_of_three_side[0]
    b = length_of_three_side[1]
    c = length_of_three_side[2]
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    return area

def main():
    '''
    variable require: None(type)

    function require:
        ask_length
        calculate

    private variable: None

    purpose: this is main function of the program

    return variable: None(type)
    '''
    
    #Be known, I didn't a triangle checking function('6 6 6' will work in this program), becuase it need quite a lot work

    side_list = ask_length()
    area = calculate(side_list)
    print('if the sides lengle of a triangle are',side_list,', then the area od the trangle is',area)

if __name__ == "__main__":
    main()