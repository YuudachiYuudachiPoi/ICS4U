'''
name: easter_variation2
This program is writen by 希理(Howie Hong)
date: 2019/2/14

purpose: This program is used for calculating the data of Easter Sunday. It will ask for user the year, 
and answer the data of Easter Sunday in the year.

libary require: None
'''

def ask_for_year():
    '''
    variable require: None

    function require: None

    private variable: year

    purpose: It will ask for user the year that user want to calculate

    return variable: year(int)
    '''

    year = input('Please enter the year that you want to calculate. ')
    year = int(year)
    return year

def calculate(year):
    '''
    variable require: year(int)

    private variable:
        a,b,c,d,e,f,g,h,i,k,j,m,p
        month,day

    function require: None

    purpose: calculate the date of the year in Easter

    return variable: month(str),day(int)
    '''

    a = year % 19
    b = year // 100 
    c = year % 100
    d = b // 4
    e = b % 4
    f = (8 + b) // 25
    g = int((b - f + 1)/3)
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    j = (32 + 2*e + 2*i - h - k)%7
    m = (a + 11*h + 22*j)//451
    month = (h + j -7*m + 114)/31
    p = (h + j - 7*m + 114)%31
    day = p + 1

    if month == 3:
        month = "March"
    else:
        month = "April"

    return month,day

def main():
    '''
    purpose: This is the main function of the program

    variable require: None

    private variable: year,month,day

    function require: 
        ask_for_year()
        calculate()

    return variable: None
    '''

    print("Easter Date Calculatorn")
    year = ask_for_year()
    month,day = calculate(year)

    print("Easter will fall on Sunday, "+month,day,",",year)

if __name__ == "__main__":
    main()