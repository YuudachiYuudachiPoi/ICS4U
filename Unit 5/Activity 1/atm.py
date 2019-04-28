#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 3019-04-28 09:45:34
LastEditTime: 2019-04-28 13:23:44
'''
class ATM():
    '''
    self.account_number{str}
    self.bank_name{str}
    self.balence{float}
    #self.daily_interest{float}
    '''
    def __init__(self,account_number):
        '''
        description: 
        param {str} 
        return: 
        '''
        import sys
        path = sys.path[0]
        try:
            data_base = open(path+'\\bank_data_base.txt','r')
            data_base.close()
        except FileNotFoundError:
            with open(path+'\\bank_data_base.txt','a') as data_base:
                #info_tuple = ('account_number','bank_name','balance','d_interest(%)','date','operation')
                info_tuple = ('account_number','bank_name','balance','operation')
                for info in info_tuple:
                    data_base.write('{:<30}'.format(info))
            #self.create_account(account_number) #test account


        account_data = self.__latest_record(account_number)
        if account_data == None:
            '''
            self.create_account(account_number) #it should let customer contact a bank branch. However,in this program, it create an account for convenience
            account_data = self.__latest_record(account_number)
            '''
        self.account_number = account_data[0]
        self.bank_name = account_data[1]
        self.balance = float(account_data[2])
        #self.daily_interest = float(account_data[3])
        #last_record_time = float(account_data[4])
        '''
        import time
        now_time = time.time()
        number_of_day = (now_time-last_record_time)//(24*60*60) #there is only one type of interest
        if number_of_day == 0:
            self.balance = old_balance
            self.__write_record('user_log_in')
        elif number_of_day > 0:
            self.balance = old_balance*(1+self.daily_interest)**number_of_day
            self.__write_record('calculate_interest')
            self.__write_record('user_log_in')
        else:
            raise Exception('The record time is in future')
        '''

    def deposit(self,amount_of_money):
        if amount_of_money > 0:
            self.balance += amount_of_money
            self.__write_record('deposit')
            return 'You deposited ${}'.format(amount_of_money)
        else:
            return 'request denied'

    def withdraw(self,amount_of_money):
        if amount_of_money > 0:
            if self.balance - amount_of_money > 0:
                self.balance -= amount_of_money
                self.__write_record('withdraw')
                return 'You withdrew ${}'.format(amount_of_money)
            else:
                return 'request denied'
        else:
            return 'request denied'
    
    def add_daily_interest(self,interest_rate,number_of_day):
        if interest_rate>0 and number_of_day>0:
            self.balance = self.balance*(1+interest_rate)**number_of_day
            self.__write_record('calculate_interest')
            #self.__write_record('user_log_in')
            return 'interest calculated, and added to you balance'
        else:
            return 'request denied'

    def current_balance(self,account_number):
        if self.__latest_record(account_number) == None:
            return 'Can not find your account'
        else:
            return self.__latest_record(account_number)[1]

    def __latest_record(self,account_number):
        '''
        description: find the lastest record of the account
        param account_number{str} 
        return: account_data{ [bank_name,balance,daily_interest,last_record_time,operation] }(all of them are str)
        '''
        import sys
        path = sys.path[0]
        with open(path+'\\bank_data_base.txt','r') as data_base:
            data = data_base.read().split('\n')[1:][::-1]  #change it to writeline method if the data is very big


        len_of_account_number = len(account_number)
        for record in data:
            if record[:len_of_account_number] == account_number:
                account_data = record.split()
                return account_data
        else:
            return None


    def create_account(self,account_number,bank_name='TD',initial_balance=5000.0,daily_interest=0.05): #constructor
        '''
        description: create a bank account
        param {str} 
        return: 
        '''
        if self.__latest_record(account_number) == None:
            self.account_number = account_number
            self.bank_name = bank_name
            self.balance = initial_balance
            #self.daily_interest = daily_interest

            self.__write_record('create_an_account')

    def __write_record(self,operation):
        '''
        description:
        param {str} 
        return: 
        '''
        import sys,time
        path = sys.path[0]
        with open(path+'\\bank_data_base.txt','a') as data_base:
            data_base.write('\n')
            data_base.write('{:<30}'.format(self.account_number))
            data_base.write('{:<30}'.format(self.bank_name))
            data_base.write('{:<30}'.format(self.balance))
            #data_base.write('{:<30}'.format(self.daily_interest))
            #data_base.write('{:<30}'.format(time.time()))
            data_base.write('{:<30}'.format(operation))
        
        
if __name__ == "__main__":
    a = ATM('123456')
    print(a.deposit(100))
    print(a.withdraw(1000))
    print(a.withdraw(10000))
    print(a.add_daily_interest(0.05,5))
    