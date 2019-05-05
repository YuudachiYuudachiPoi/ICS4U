
class ComboLock():
    '''
    description: 
    param:
        __num1{int}
        __num2{int}
        __num3{int} 
    return: 
    '''
    def __init__(self,num1=None,num2=None,num3=None):
        '''
        description: 
        param {all int or all None} 
        return: 
        '''
        import random
        if num1 == None:
            self.__num1 = random.randint(1,3)
            self.__num2 = random.randint(1,3)
            self.__num3 = random.randint(1,3)
        else:   
            self.__num1 = num1
            self.__num2 = num2
            self.__num3 = num3
    def check_numbers(self,num1,num2,num3):
        if self.__num1 == num1 and self.__num2 == num2 and self.__num3 == num3:
            return True
        else:
            return False

    def __str__(self):
        return str(self.__num1)+' '+str(self.__num2)+' '+str(self.__num3)