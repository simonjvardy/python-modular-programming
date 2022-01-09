"""
Data Storage Module functions
"""
import json
import os.path


def init():
    """init function to load the inventory items data"""
    _load_items()


def items():
    """Makes the inventory items data stored in memory available to the user"""
    global _items
    return _items


def products():
    """Makes the procuct items list stored in memory available to the user"""
    global _products
    return _products


def locations():
    """Makes the locations list stored in memory available to the user"""
    global _locations
    return _locations


def add_item(product_code, location_code):
    """Add new product items to the stored list"""
    global _items
    _items.append((product_code, location_code))
    _save_items()


def remove_item(product_code, location_code):
    """Delete product items from the stored list"""
    global _items
    for i in range(len(_items)):
        prod_code,loc_code = _items[i]
        if prod_code == product_code and loc_code == location_code:
            del _items[i]
            _save_items()
            return True  # Returns True if the deletion was successful
        return False  # Returns False if the deletion was unsuccessful


def set_products(products):
    """Sets the list of procuct items to memory"""
    global _products
    _products = products


def set_location(locations):
    """Sets the list of locations to memory"""
    global _locations
    _locations = locations


def _load_items():
    """Load the items data from a JSON file"""
    global _items
    if os.path.exists("items.json"):
        f = open("items.json", "r")
        _items = json.loads(f.read())
        f.close()
    else:
        _items = []


def _save_items():
    """Save the list of inventory items to disk"""
    global _items
    f = open("items.json", "w")
    f.write(json.dumps(_items))
    f.close
