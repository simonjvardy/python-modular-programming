"""
Data Storage Module functions
"""
import json
import os.path


def init():
    """"""
    _load_items()


def items():
    """"""
    global _items
    return _items


def products():
    """"""
    pass


def locations():
    """"""
    pass


def add_item(product_code, location_code):
    """"""
    pass


def remove_item(product_code, location_code):
    """"""
    pass


def set_products(products):
    """"""
    pass


def set_location(locations):
    """"""
    pass


def _load_items():
    """Load the items data from a JSON file"""
    global _load_items
    if os.path.exists("items.json"):
        f = open("items.json", "r")
        _items = json.loads(f.read())
        f.close()
    else:
        _items = []


def _save_items():
    """Save the list of inventory items to disk"""
    global _load_items
    f = open("items.json", "w")
    f.write(json.dumps(_items))
    f.close
