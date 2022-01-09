"""
User Interface Module functions
"""

import datastorage


def prompt_for_action():
    """
    Function to generate a command-line user interface.
    Not the best way to implement it, but it works!
    """
    while True:
        print()
        print("WHat would you like to do?")
        print()
        print("  A = add an item to the inventory.")
        print("  R = remove an item from the inventory.")
        print("  C = generate a report of the current inventory levels.")
        print("  O = generate a report of the inventory items to re-order.")
        print("  Q = quit.")
        print()
        action = input("> ").strip().upper()
        if action == "A":
            return "ADD"
        elif action == "R":
            return "REMOVE"
        elif action == "C":
            return "INVENTORY_REPORT"
        elif action == "O":
            return "REORDER_REPORT"
        elif action == "Q":
            return "QUIT"
        else:
            print("Unknown action!")


def prompt_for_product():
    """
    Function to display a list of products with a number beside
    each product. The user enters the number of the desired product.
    The function then returns the product code to the caller.
    """
    while True:
        print()
        print("Select a product:")
        print()
        n = 1
        for code,description,desired_number in datastorage.products():
            print("  {}. {} - {}".format(n, code, description))
            n = n + 1

        s = input("> ").strip()
        if s == "":
            return None
        
        try:
            n = int(s)
        except ValueError:
            n = -1

        if n < 1 or n > len(datastorage.products()):
            print("Invalid option: {}".format(s))
            continue

        product_code = datastorage.products()[n-1][0]
        return product_code


def prompt_for_location():
    """
    Function to display a list of locations with a number beside
    each location. The user enters the number of the desired location.
    The function then returns the location code to the caller.
    """
    while True:
        print()
        print("Select a location:")
        print()
        n = 1
        for code,description in datastorage.locations():
            print("  {}. {} - {}".format(n, code, description))
            n = n + 1

        s = input("> ").strip()
        if s == "":
            return None
        
        try:
            n = int(s)
        except ValueError:
            n = -1

        if n < 1 or n > len(datastorage.locations()):
            print("Invalid option: {}".format(s))
            continue

        location_code = datastorage.locations()[n-1][0]
        return location_code


def show_report(report):
    """
    Function to show the generated reports to the user
    """
    print()
    for line in report:
        print(line)
    print() 



def show_error(err_msg):
    """
    Very simple error handling function for
    user input errors feedback
    """
    print()
    print(err_msg)
    print()
