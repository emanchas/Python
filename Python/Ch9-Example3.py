class Phone:

    def __init__(self, model, price):
        self.__model = model
        self.__price = price

    def set_price(self, price):
        self.__price = price

    def set_model(self, model):
        self.__model = model

    def get_price(self):
        return self.__price
    def get_model(self):
        return self.__model

class Customer:
    def __init__(self, name):
        self.__name = name
        self.item_list = []

    def add_item(self, phone):
        self.item_list.append(phone)

    def get_name(self):
        return self.__name

    def get_item(self):
        total_cost = 0
        for item in self.item_list:
            print('Phone Model:', item.get_model())
            print('Phone price:', item.get_price())
            total_cost = total_cost + item.get_price()
        return total_cost

    def add_item(self, item):
        self.item_list.append(item)
        
    def remove_item(self, model):
        for item in self.item_list:
            if item.get_model() == model:
                self.item_list.remove(item)


def main():
    me = Customer('Me')
    you = Customer('You')

    num_of_phone = int(input('Enter the number of phones I want to purchase: '))

    for count in range(num_of_phone):
        model = input('Phone Model: ')
        price = int(input('Phone Price: '))
        phone = Phone(model, price) #create an object of Phone class
        me.add_item(phone)

    #calculate the total cost
    my_cost = me.get_item()
    print('Customer', me.get_name(), 'is: $', my_cost)

    print ('Remove some models')
    model = input('What model do you want to remove? ')
    me.remove_item(model)
    my_cost = me.get_item()
    print ('Customer', me.get_name(), 'is: $', my_cost)
      


main()
