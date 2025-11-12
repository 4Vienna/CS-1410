from dessert import Candy, Cookie, IceCream, Sundae, Order 
from payment import Payable
from tabulate import tabulate


class DessertShop:
    def user_prompt_candy(self):
        '''Prompts the user for candy details and returns a Candy object'''
        name = input("Enter the name of the candy: ")
        while True:
            try:
                weight = float(input("Enter weight (lbs): "))
                if weight < 0:
                    raise ValueError("Weight cannot be negative")
                break
            except ValueError as e:
                print(f"Caught a ValueError: {e}.\nPlease enter a positive numeric value for weight")
        while True:
            try:
                price_per_pound = float(input("Enter the price per pound: "))
                if price_per_pound < 0:
                    raise ValueError("price cannot be negative")
                break
            except ValueError as e:
                print(f"Caught a ValueError: {e}.\nPlease enter a positive numeric value for weight")

        return Candy(name, weight, price_per_pound)

    def user_prompt_cookie(self):
        """Prompts the user for cookie details and returns a Cookie object"""
        name = input("Enter the name of the cookie: ")
        while True:
            try:
                number_of_cookies = int(input("Enter the number of cookies: "))
                if number_of_cookies < 0:
                    raise ValueError("Number of cookies cannot be negative")
                break
            except ValueError as e:
                print(f"Caught a ValueError: {e}.\nPlease enter a positive integer value for number of cookies")

        while True:
            try:
                price_per_dozen = float(input("Enter the price per dozen: "))
                if price_per_dozen < 0:
                    raise ValueError("Price per dozen cannot be negative")
                break
            except ValueError as e:
                print(f"Caught a ValueError: {e}.\nPlease enter a positive numeric value for price per dozen")
        return Cookie(name, number_of_cookies, price_per_dozen) 

    def user_prompt_icecream(self):
        """Prompts the user for ice cream details and returns an IceCream object"""
        name = input("Enter the name of the ice cream: ")
        while True:
            try:
                scoop_count = int(input("Enter the number of scoops: "))
                if scoop_count < 0:
                    raise ValueError("Number of scoops cannot be negative")
                break
            except ValueError as e:
                print(f"Caught a ValueError: {e}.\nPlease enter a positive numeric value for number of scoops")

        while True:
            try:
                price_per_scoop = float(input("Enter the price per scoop: "))
                if price_per_scoop < 0:
                    raise ValueError("Price per scoop cannot be negative")
                break
            except ValueError as e:
                print(f"Caught a ValueError: {e}.\nPlease enter a positive numeric value for price per scoop")
        return IceCream(name, scoop_count, price_per_scoop)

    def user_prompt_sundae(self):
        """Prompts the user for sundae details and returns a Sundae object"""
        name = input("Enter the type of icecream: ")
        while True:
            try:
                scoop_count = int(input("Enter the number of scoops: "))
                if scoop_count < 0:
                    raise ValueError("Number of scoops cannot be negative")
                break
            except ValueError as e:
                print(f"Caught a ValueError: {e}.\nPlease enter a positive numeric value for number of scoops")

        while True:
            try:
                price_per_scoop = float(input("Enter the price per scoop: "))
                if price_per_scoop < 0:
                    raise ValueError("Price per scoop cannot be negative")
                break
            except ValueError as e:
                print(f"Caught a ValueError: {e}.\nPlease enter a positive numeric value for price per scoop")

        topping_name = input("Enter the name of the topping: ")
        while True:
            try:
                topping_price = float(input("Enter the price of the topping: "))
                if topping_price < 0:
                    raise ValueError("Price of topping cannot be negative")
                break
            except ValueError as e:
                print(f"Caught a ValueError: {e}.\nPlease enter a positive numeric value for price of topping")

        return Sundae(name, scoop_count, price_per_scoop, topping_name, topping_price)
    
    def payment(self):
        pay = '\n'.join([ '\n',
            '1: CASH',
            '2: CARD',            
            '3: PHONE',
            '\nEnter payment method (1-3): '
      ])
        while True:
            choice = input(pay)
            match choice:
                case '1':
                    payment_method = "CASH"
                    DessertShop().payment()
                    break
                case '2':
                    payment_method = "CARD"
                    break
                case '3':
                    payment_method = "PHONE"
                    break
                case _:
                    print('Invalid response:  Please enter a choice from the menu (1-3)')

def main():
    shop = DessertShop() 
    order = Order()
    
    # order.add(Candy('Candy Corn', 1.5, 0.25))
    # order.add(Candy('Gummy Bears', 0.25, 0.35))
    # order.add(Cookie('Chocolate Chip', 6, 3.99))
    # order.add(IceCream('Pistachio', 2, 0.79))
    # order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    # order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
            '1: Candy',
            '2: Cookie',            
            '3: Ice Cream',
            '4: Sundae',
            '\nWhat would you like to add to the order? (1-4, Enter for done): '
      ])

    while not done:
      choice = input(prompt)
      match choice:
        case '':
          done = True
        case '1':            
          item = shop.user_prompt_candy()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '2':            
          item = shop.user_prompt_cookie()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '3':            
          item = shop.user_prompt_icecream()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '4':            
          item = shop.user_prompt_sundae()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case _:            
          print('Invalid response:  Please enter a choice from the menu (1-4) or Enter')
    print()
    
    # Add your code below here to print the receipt as the last thing in main()
    # Make sure that the output format matches the provided sample run
    headers = ["Name", "Cost", "Tax"]

    # Build rows using Order.to_list which now returns multiple rows per item
    rows = order.to_list()

    # Print the table. Use plain format so the multi-line layout looks like the sample.
    print(tabulate(rows, headers = headers, tablefmt="plain", colalign=("left","right","left")))

    # Print totals similar to the sample layout
    print('-' * 31 + '  ' + '-' * 10 + '  ' + '-' * 12)
    print(f"Total number of items in order:  {len(order)}")
    print(f"Order Subtotals:                 ${order.order_cost():.2f}       [Tax: ${order.order_tax():.2f}]")
    print(f"Order Total:                                 ${order.order_cost() + order.order_tax():.2f}")
    print('-' * 31 + '  ' + '-' * 10 + '  ' + '-' * 12)
    

if __name__ == "__main__":
    main()