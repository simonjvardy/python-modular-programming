"""
Main Program
"""

import datastorage
import userinterface
import reportgenerator


def main():
    """
    Function to initiate the program and load the
    example data into memory.
    """
    datastorage.init()  # Load the JSON data into memory

    """
    Build the example products list data
    """
    datastorage.set_products([
        ("SKU123", "4 mm flat-headed wood screw", 50),
        ("SKU145", "6 mm flat-headed wood screw", 50),
        ("SKU167", "4 mm countersunk head wood screw", 10),
        ("SKU169", "6 mm countersunk head wood screw", 10),
        ("SKU172", "4 mm metal self-tapping screw", 20),
        ("SKU185", "8 mm metal self-tapping screw", 20),
    ])

    """
    Build the example locations data
    """
    datastorage.set_location([
        ("S1A1", "Shelf 1, Aisle 1"),
        ("S2A1", "Shelf 2, Aisle 1"),
        ("S3A1", "Shelf 3, Aisle 1"),
        ("S1A2", "Shelf 1, Aisle 2"),
        ("S2A2", "Shelf 2, Aisle 2"),
        ("S3A2", "Shelf 3, Aisle 2"),
        ("BIN1", "Storage Bin 1"),
        ("BIN2", "Storage Bin 2"),
    ])

    # Ask the user for the action to be performed
    while True:
        action = userinterface.prompt_for_action()

        if action == "QUIT":
            break
        elif action == "ADD":
            product = userinterface.prompt_for_product()
            if product is not None:
                location = userinterface.prompt_for_location()
                if location is not None:
                    datastorage.add_item(product, location)
        elif action == "REMOVE":
            product = userinterface.prompt_for_product()
            if product is not None:
                location = userinterface.prompt_for_location()
                if location is not None:
                    if not datastorage.remove_item(product, location):
                        pass  # What to do?

if __name__ == "__main__":
    main()
