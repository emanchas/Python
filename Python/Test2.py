
class ItemToPurchase:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def get_quantity(self):
        return self.__quantity
    def get_item_cost(self):
        return self.__price * self.__quantity

class Customer:
    def __init__(self, name, date):
        self.__name = name
        self.__date = date
        self.shopping_cart = []

    def get_name(self):
        return self.__name
    def get_date(self):
        return self.__date
    def add_item(self, item):
        self.shopping_cart.append(item)

    def remove_item(self, name):
        found = 0
        for item in self.shopping_cart:
            if item.get_name() == name:
                self.shopping_cart.remove(item)
                print(item.get_name(), 'has been removed from shopping cart.')
                found = 1
        if found == 0:
            print('Item not found; no item removed.')
                
    def check_out(self):
        print()
        print('Checking out')
        print('Customer Name:', self.__name)
        print('Transaction date:', self.__date)
        total = 0
        for item in self.shopping_cart:
            total += item.get_item_cost()
            print(item.get_quantity(), item.get_name(), ' @ $', item.get_price())
        print('Total Amount: $', total)

def main():
    cus_name = input('Enter Customer Name: ')
    date = input('Enter Shopping Date: ')
    customer = Customer(cus_name, date)

    add_number = int(input('How many items does the customer add into shopping cart? '))
    for i in range(add_number):
        print('Item #', i+1, sep='')
        item_name = input('Item Name: ')
        item_price = float(input('Item Price: '))
        item_quantity = float(input('Item Quantity: '))
        item = ItemToPurchase(item_name, item_price, item_quantity)
        customer.add_item(item)

    remove_number = int(input('How many items does the customer remove from the shopping cart? '))
    for i in range(remove_number):
        item_name = input('Item name for removing: ')
        customer.remove_item(item_name)

    customer.check_out()

main()

        
            
                      
            
    
    
