#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
Date: 2019-05-26 12:13:32
LastEditors: Howie Hong(希理)
LastEditTime: 2019-05-26 12:53:43
Description: the CellPhone class file
'''
class CellPhone:
    '''
    description: a cell phone class
    param: 
        __carrier,__type{str}
        __speed, __memory{float}
        __num_apps{int} 
    '''
    
    def __init__(self,type,speed,memory):
        '''
        description: set carrier and type 
        param: 
            type{str} 
            speed{float}
            memory{float}
        return: 
        '''
        
        if isinstance(type,str):
            self.__type = type
        else:
            print('Invalid Type')
            self.__type = 'Unknown'
            
        if isinstance(speed,float):
            self.__speed = speed
        else:
            print('Invalid Speed')
            self.__speed = 0.0
        
        if isinstance(memory,float):
            self.__memory = memory
        else:
            print('Invalid Memory')
            memory = 0.0


    def set_carrier(self,carrier):
        '''
        description: 
        param {str} 
        return: 
        '''
        if isinstance(carrier,str):
                self.__carrier = carrier
        else:
            print('Invalid Carrier')
            self.__carrier = 'Unknown'
            
    def get_carrier(self):
        '''
        description: 
        param {type} 
        return: __carrier{str}
        '''
        return self.__carrier
    
    def get_type(self):
        '''
        description: 
        param {type} 
        return: __type{str}
        '''        
        return self.__type
    
    def set_num_apps(self,num_apps):

        if isinstance(num_apps,int):
            self.__num_apps = num_apps
        else:
            print('Invalid Number of Apps')
    
    def get_num_apps(self):
        return str(__nums_apps)

    def __str__(self):
        message = ("Carrier = " + self.__carrier +'\n')
        message += ("Type of phone = " + self.__type +'\n')
        message += ("Speed of phone = " + str(self.__speed) + "Ghz" +'\n')
        message += ("Memory = " + str(self.__memory) + "Gb" +'\n')
        message += ("Number of Apps = " + str(self.__num_apps) +'\n')

        return message