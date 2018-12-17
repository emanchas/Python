
class ItemToPurchase:

    def __init__(self, name='none', price=0, quantity=0, description='none'):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def set_item_name(self, name):
        self.item_name = name
    def set_item_price(self, price):
        self.item_price = price
    def set_item_description(self, description):
        self.item_description = description
    def set_item_quantity(self, quantity):
        self.item_quantity = quantity
    def set_itemDescription(self, description):
        self.item_description = description

    def get_item_cost(self):
        return self.item_price * self.item_quantity

    def print_item_cost(self):
        print(self.item_name, ' ', self.item_quantity, ' @ $', self.item_price, ' = $',
              self.get_item_cost(), sep='')

    def print_item_description(self):
        print(self.item_name, ':', self.item_description)


class ShoppingCart:
    def __init__(self, name, date):
        self.customer_name = name
        self.date = date
        self.cart_item = []

    def add_item(self, add_item):
        self.cart_item.append(add_item)

    def remove_item(self, target_name):
        found = 'false'
        for item in self.cart_item:
            if item.item_name == target_name:
                self.cart_item.remove(item)
                found = 'true'
        if found == 'false':
            print('Item not found in cart.')

    def modify_item(self, name, quantity):
        found = 'false'
        for item in self.cart_item:
            if item.item_name == name:
                item.set_item_quantity(quantity)
                found = 'true'
        if found == 'false':
            print('Item not found in cart.')

    def get_num_items_in_cart(self):
        total_num = 0
        for item in self.cart_item:
            total_num += item.item_quantity
        return total_num

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_item:
            total_cost += item.get_item_cost()
        return total_cost

    def print_total(self):
        print(self.customer_name, "\' Shopping Cart - ", self.date, sep='')
        print('Number of Item:', self.get_num_items_in_cart())
        for item in self.cart_item:
            item.print_item_cost()
        print('Total: $', self.get_cost_of_cart(), sep='')

    def print_description(self):
        print(self.customer_name, "\' Shopping Cart - ", self.date, sep='')
        if len(self.cart_item) > 0:
            for item in self.cart_item:
                item.print_item_description()
        else:
            print('Shopping Cart is empty.')
        

def print_menu(cart):
    option = 'x'
    while option != 'q':
        print('a - Add an item to your cart')
        print('r - Remove an item from cart')
        print('c - Change item quantity')
        print("i - Output item(s) description(s)")
        print('o - Output shopping cart')
        print('q - Quit')
        option = input('Choose an option: ')
        while option != 'a' and option != 'r' and option != 'c' and option != 'i' and \
        option != 'o' and option != 'q':
            option = input('Choose an option: ')
        if option == 'a':
            print('You selected: Add item to cart')
            name = input('Enter the item name: ')
            price = float(input('Enter the item price (Do not include $ symbol): '))
            quantity = int(input('Enter the item quantity: '))
            description = input('Enter item description: ')
            item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(item)
        if option == 'r':
            print('You selected: Remove item from cart')
            name = input('Enter name of item to remove: ')
            cart.remove_item(name)
        if option == 'c':
            print('You selected: Change item quantity')
            name = input('Enter the item name: ')
            quantity = int(input('Enter the new quantity: '))
            cart.modify_item(name, quantity)
        if option == 'i':
            cart.print_description()
        if option == 'o':
            cart.print_total()
        if option == 'q':
            print ('Thank you for shopping with !')

    

def main():
    name = input("Enter customer name: ")
    date = input("Enter today's date: ")
    cart1 = ShoppingCart(name, date)
    cart1.print_description()

    print_menu(cart1)

main()
    
