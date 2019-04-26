#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-04-26 08:50:51
LastEditTime: 2019-04-26 11:51:37
'''
class Car:
    '''
    make{str}
    model{str}
    price{int}
    number_of_seat{int}
    gps_build_in{boolean} 
    '''
    def __init__(self,make=None,model=None,year=None,price=None,number_of_seat=None,gps_build_in=None):
        '''
        description: 
        param: 
            make{str}
            model{str}
            price{int}
            number_of_seat{int}
            gps_build_in{boolean} 
        return: 
        '''
        import random
        if make == None:
            self.make = random.choice(['Alfa Romeo','Audi','Aston Martin','BMW','Bentley','Buick','Bugatti','Cadillac','Chrysler','Citroen','Chevrolet','Daewoo','Daihatsu','Dodge','Ferrari','Fiat','Ford','Honda','Hyundai','Hummer','ISUZU','Jaguar','Jeep','Kia','Land Rover','Lexus','Lincoln','Lamborghini'])
        else:
            self.make = make

        if model == None:
            self.model = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','1','2','3','4','5','6','7','8','9','0'], 5))
        else:
            self.model = model

        if year == None:
            import datetime
            self.year = random.randint(1980,datetime.datetime.now().year)
        else:
            self.year = year
        
        if price == None:
            self.price = random.randint(3000,3000000)
        else:
            self.price = price
        
        if number_of_seat == None:
            self.number_of_seat = random.choice([2,5,7])
        else:
            self.number_of_seat = number_of_seat
        
        if gps_build_in == None:
            self.gps_build_in = random.choice([True,False])
        else:
            self.gps_build_in = gps_build_in
    
    def __str__(self):
        message = '\nmodel: {} \nmake: {} \nyear: {} \nnumber of seat: {} \n'.format(self.model,self.make,self.year,self.number_of_seat)
        if self.gps_build_in:
            message += 'gps build in: Yes\n'
        else:
            message += 'gps build in: No\n'
        
        return message

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