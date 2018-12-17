
class Automobile:
    def __init__(self, maker, model, price):
        self.__maker = maker
        self.__model = model
        self.__price = price
    def get_maker(self):
        return self.__maker
    def get_model(self):
        return self.__model
    def get_price(self):
        return self.__price

class Car(Automobile):
    def __init__(self, maker, model, price, door_num):
        Automobile.__init__(self, maker, model, price)
        self.__door_num = door_num

    def get_door_num(self):
        return self.__door_num

class SUV(Automobile):
    def __init__(self, maker, model, price, drive_type):
        Automobile.__init__(self, maker, model, price)
        self.__drive_type = drive_type

    def get_drive_type(self):
        return self.__drive_type


def main():
    my_car = Car('Toyota', '2016', 22000, 4)

    print ('Car:')
    print ('Maker:', my_car.get_maker())
    print ('Model:', my_car.get_model())
    print ('Price:', my_car.get_price())
    print ('Doors:', my_car.get_door_num())
    print ('')
    
    my_SUV = SUV('Kia', '2016', 18000, '4WD')

    print ('SUV:')
    print ('Maker:', my_SUV.get_maker())
    print ('Model:', my_SUV.get_model())
    print ('Price:', my_SUV.get_price())
    print ('Drive type:', my_SUV.get_drive_type())
    print ('')
    
    
main()
        
