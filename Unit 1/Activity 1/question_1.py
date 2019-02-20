import math

#----------------------------------------------------
#a
'''
math.sqrt(x) will return a square root of x
For example, square root of 9 is 3
3^2 = 9
3*3*3 = 9
'''

print(math.sqrt(9) == 3) #it will print out True
print(math.sqrt(9) != 3) #it will print out False
print(math.sqrt(4) == 2) #it will print out True
print(math.sqrt(4) != 2) #it will print out False

print()
#----------------------------------------------------
#b
'''
math.cos() will Return the arc cosine (measured in radians) of x.
2pi rad == 360 degree

For example, the side length of a triangle are '3 4 5'(right triangle)
I want to know each agree of the triangle
'''

print(math.acos(3/5)) #To be noted that it is measured in radians
print(math.acos(3/5) /math.pi *180) #To get the measurement in degree
print(math.acos(4/5))
print(math.acos(4/5) /math.pi *180)

print()
#---------------------------------------------------------------------------
#c
'''
math.ceil(x) will return the ceiling of x as an Integral.

This is the smallest integer >= x.
'''
#For example
print(math.ceil(-45.17)) #it will print out -45
print(math.ceil(100.12)) #it will print out 101
print(math.ceil(100.72)) #it will print out 101

print()
#---------------------------------------------------------------------------
#d
'''
math.pi = 3.14........
For example, I want to calculate the area of a circle, 
and the r of the circle is 2.
'''

print(2**2 *math.pi) # s = pi*(r^2)
print(2**2 *3.14) # it is better to use math.pi, because it is more accuracy