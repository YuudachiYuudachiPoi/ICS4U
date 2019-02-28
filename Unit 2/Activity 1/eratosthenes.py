'''
name: eratosthenes

This program is writen by 希理(Howie Hong)

date: 2019/2/25

purpose: the impoved ver. of eratothenes_old
    this program will only go thought the list once

libary require: None
'''

divider_list = [2]
for num in range(2,1000):#you can change the second number to a number that greater than 2
    for divider in divider_list:
        if num%divider == 0:
            break
    else: #if the num isn't multiple of all existed dividers
        divider_list.append(num)
        print(num) #  comment this line if you want line breaks

''' #uncomment it will you want line breaks
for i,num in enumerate(divider_list):
    print('{:<4d}'.format(num),end='')
    if (i+1)%7 == 0: #7 is num of num in each line,you can change it
        print()
'''