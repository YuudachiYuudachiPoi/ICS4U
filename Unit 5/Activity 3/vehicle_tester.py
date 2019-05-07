#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-05-07 12:27:21
LastEditTime: 2019-05-07 13:11:27
'''
import sys
path = sys.path[0]
sys.path.append(path)
import vehicle


passengers = int(input('How many passengers? '))

passenger_fare = float(input('Passenger fare? '))

gas_price = float(input('What is the price of gas today in $/L ? '))

car1 = vehicle.Vehicle(7.5, 60.0, 60.0, 0.0,passengers,passenger_fare,gas_price)
#Show Vehicle Info
print('\n')
print(car1)


print('Revenue =',car1.revenue())
gas_start = car1.fuel_available
#Drive car for 100km
car1.drive_vehicle(100.0)
print(car1)

#Drive car for 450 kms
car1.drive_vehicle(450.0)
print(car1)

#Try to drive 1000 km - runs out of gas
car1.drive_vehicle(1000.0)
print(car1)

#Add 25L of gas
car1.add_fuel(25.0)
print(car1)

#Try to add 100 L of gas
car1.add_fuel(100.0)
print(car1)

print('Revenue =',car1.revenue())
print('Cost =',car1.total_costs())
print('Profit =',car1.profits())