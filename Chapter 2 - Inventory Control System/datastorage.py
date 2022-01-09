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
    """Add new product items to the stored list"""
    global _items
    _items.append((prodict_code, location_code))
    _save_items()


def remove_item(product_code, location_code):
    """Delete product items from the stored list"""
    global _items
    for i in range(len(_items)):
        prod_code,loc_code = _items[i]
        if prod_code == product_code and loc_code == location_code:
            del _items[i]
            _save_items()
            return True
        return False


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
