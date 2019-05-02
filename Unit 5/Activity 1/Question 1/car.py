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
