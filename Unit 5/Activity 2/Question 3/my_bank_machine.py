#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
LastEditors: Howie Hong(希理)
Description: 
Date: 2019-04-28 13:23:01
LastEditTime: 2019-04-28 15:01:31
'''
import sys,os
path = sys.path[0]
sys.path.append(path)
import atm



while True:
    answer = 0
    while not answer in [1,2,3]:
        os.system('cls')
        try:
            answer = int(input('\n1 - Log in\n2 - Create a account\n3 - Exit\n'))
        except:
            pass
        
    if answer == 1:
        os.system('cls')
        account_number = input('Account number: ')
        link = atm.ATM(account_number)
        if link.account_exist(account_number):
            answer = 0
            while answer != 4:
                answer = 0
                while not answer in [1,2,3,4]:
                    os.system('cls')
                    print('Current balance: $'+link.current_balance())
                    try:
                        answer = int(input('\n1 - Deposit\n2 - Withdraw\n3 - Add daily interest\n4 - exit\n'))
                    except:
                        pass
                
                if answer == 1:
                    amount_of_money = 0
                    while not amount_of_money > 0:
                        os.system('cls')
                        print('Current balance: $'+link.current_balance())
                        try:
                            amount_of_money = float(input('Amount of money you want to deposit: '))
                        except:
                            pass
                    print(link.deposit(amount_of_money))
                    input('enter to continue ')
                elif answer == 2:
                    amount_of_money = 0
                    while not amount_of_money > 0:
                        os.system('cls')
                        print('Current balance: $'+link.current_balance())
                        try:
                            amount_of_money = float(input('Amount of money you want to withdraw: '))
                        except:
                            pass
                    print(link.withdraw(amount_of_money))
                    input('enter to continue ')
                elif answer == 3:
                    interest_rate = 0
                    while not interest_rate > 0:
                        os.system('cls')
                        print('Current balance: $'+link.current_balance())
                        try:
                            interest_rate = float(input('What is the rate of interest?(in %) '))
                        except:
                            pass

                    number_of_day = 0
                    while not number_of_day > 0:
                        try:
                            number_of_day = int(input('How many days to leave balance inverted? '))
                        except:
                            pass

                    print(link.add_daily_interest(interest_rate,number_of_day))
                    input('enter to continue ')
        else:
            print('The account is not exist(enter to continue)')
            input()
            continue
    elif answer == 2:
        os.system('cls')
        account_number = input('Account number: ')
        link = atm.ATM(account_number)
        if link.account_exist(account_number):
                print('The account already exist(enter to continue)')
                input()
                continue
        bank_name = input('Bank name: ')
        init_balance = 0
        while not init_balance>0:
            os.system('cls')
            print('Account number: '+account_number)
            print('Bank name: '+bank_name)
            try:
                init_balance = int(input('initial balance: '))
            except:
                pass
        link.create_account(account_number,bank_name,init_balance)

    else:
        break