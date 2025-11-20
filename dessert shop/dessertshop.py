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

    def user_prompt_payment(self):
        """Prompt the user for payment method and return one of 'CASH','CARD','PHONE'.

        Keeps prompting until the user selects a valid menu option.
        """
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
                    return 'CASH'
                case '2':
                    return 'CARD'
                case '3':
                    return 'PHONE'
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
    # prompt for payment, validate, and set it on the order before printing
    payment_method = shop.user_prompt_payment()
    order.payment(payment_method)
    # Add your code below here to print the receipt as the last thing in main()
    # Make sure that the output format matches the provided sample run
    headers = ["Name", "Cost", "Tax"]

    # Build rows using Order.to_list which now returns multiple rows per item
    rows = order.to_list()

    # Build column widths and print a nicely aligned receipt with separators
    cols = [headers] + rows
    col_count = 3
    widths = [0] * col_count
    for c in range(col_count):
        widths[c] = max(len(str(cols[r][c])) for r in range(len(cols)))

    # top full-width separator
    top_sep = '-' * widths[0] + '  ' + '-' * widths[1] + '  ' + '-' * widths[2]
    print(top_sep)

    # header line
    header_line = headers[0].ljust(widths[0]) + '  ' + headers[1].rjust(widths[1]) + '  ' + headers[2].rjust(widths[2])
    print(header_line)

    # header underline: short left block (10 dashes) then full dashes for numeric columns
    left_dash = 10 if widths[0] >= 10 else widths[0]
    header_uline = ('-' * left_dash).ljust(widths[0]) + '  ' + ('-' * widths[1]) + '  ' + ('-' * widths[2])
    print(header_uline)

    # body rows
    for r in rows:
        name = str(r[0]).ljust(widths[0])
        cost = str(r[1]).rjust(widths[1])
        tax = str(r[2]).ljust(widths[2])
        print(name + '  ' + cost + '  ' + tax)

    # separator before totals
    print(header_uline)

    # Totals: count, subtotal/tax, and order total
    total_items_label = 'Total number of items in order:'
    print(total_items_label.ljust(widths[0]) + '  ' + str(len(order)).rjust(widths[1]) + '  ' + ''.rjust(widths[2]))

    subtotal_label = 'Order Subtotals:'
    subtotal = f"${order.order_cost():.2f}"
    taxstr = f"[Tax: ${order.order_tax():.2f}]"
    print(subtotal_label.ljust(widths[0]) + '  ' + subtotal.rjust(widths[1]) + '  ' + taxstr.ljust(widths[2]))

    total_label = 'Order Total:'
    total_amount = f"${order.order_cost() + order.order_tax():.2f}"
    combined_width = widths[1] + 2 + widths[2]
    print(total_label.ljust(widths[0]) + '  ' + total_amount.rjust(combined_width))

    # small separator and payment line
    print('-' * 20)
    print(f"Paid with {order.payment()}")
    print(top_sep)

if __name__ == "__main__":
    main()