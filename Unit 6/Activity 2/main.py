#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
Date: 2019-05-17 13:52:20
LastEditors: Howie Hong(希理)
LastEditTime: 2019-05-17 16:46:21
Description: 
'''
import sys
path = sys.path[0]
sys.path.append(path)
import animal_shelter

num_of_dogs = int(input('How many dogs will start in the shelter? '))

shelter = animal_shelter.AnimalShelter(num_of_dogs)
while True:
  print ()
  print ("Hello operator, what will you do?")
  print ("1 - Display dogs")
  print ("2 - Add a dog")
  print ("3 - Remove a dog")
  print ("4 - Display shelter costs")
  print ("5 - Exit shelter")
  choice = input ("Choose an option(1-5): " )
  if choice == "1":
    # display list of dogs
    shelter.display_dogs()
  elif choice == "2":
    # add a dog object
    shelter.add_a_dog()
  elif choice == "3":
    # remove a dog object
    shelter.remove_a_dog()
  elif choice == "4":
    # display the operating cost
    shelter.display_shelter_costs()
  elif choice == "5":
    print("\nGoodbye.")
    break
  else:
    print ("Invalid input\n")
 