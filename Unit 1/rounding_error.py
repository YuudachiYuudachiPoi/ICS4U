import math,sys
try:
    num = float(input('Please enter a number: '))
except:
    print('Please input a real.')
root = math.sqrt(num)
print('The square root of your number is:',root)
answer = root**2
print(root,'squared is:',answer)
error = num-answer
print('The round off error is:',error)