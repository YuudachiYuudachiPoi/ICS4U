#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-04-26 08:50:51
LastEditTime: 2019-04-30 10:59:55
'''

import sys
path = sys.path[0]
sys.path.append(path)
from car import *


print('Creating the first car.\n')
make = input("What is the car's made? ")
if make == '':
    make = None

model = input("What is the car's model? ")
if model == '':
    model = None

year = input("When is the car made?(year) ")

if year.isdigit():
    year = int(year)
else:
    print('year is unrecognized, it will random generate.')
    year = None

price = input("How much is it? ")
if price.isdigit():
    price =int(price)
else:
    print('price is unrecognized, it will random generate.')
    price = None

number_of_seat = input("How many seats are there? ")
if number_of_seat.isdigit():
    number_of_seat = int(number_of_seat)
else:
    print("Can't recognize your answer, it will random generate")
    number_of_seat = int(number_of_seat)

gps_build_in = input("Is there a gps build in to it?(y or n) ")
if gps_build_in.lower() == 'y':
    gps_build_in = True
elif gps_build_in.lower() == 'n':
    gps_build_in = False
else:
    print("Can't recognize your answer, it will random generate")
    gps_build_in = None

car1 = Car(make,model,year,price,number_of_seat,gps_build_in)
print(str(car1)+'\n')
print('Creating the second car.(random)')
car2 = Car()
print(str(car2))