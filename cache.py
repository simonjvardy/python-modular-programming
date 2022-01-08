"""
Create a basic cache module as part of a modular programming
design in Python.
Uses the datetime module to calculate the least recently used
entry in the cache of max. 100 values.
Credit: Erik Westra "Modular Programming with Python", Packt Publishing, 2016.
"""

import datetime

MAX_CACHE_SIZE = 100

def init():
    """
    Define a global variable internal to the cache module
    and set it as an empty dictionary.
    """
    global _cache
    _cache = {}  # Maps key to (datetime, value) tuple


def set(key, value):
    """
    Function to use the _cache variable to store an entry
    in the cache.
    """
    global _cache
    """ If new entry exceeds max cache size, remove the oldest entry """
    if key not in _cache and len(_cache) >= MAX_CACHE_SIZE:
        _remove_oldest_entry()
    _cache[key] = [datetime.datetime.now(), value]


def get(key):
    """
    Gets the cache entry value for the key argument and udates the cache entry
    with the current datetime value to show when the entry was last used.
    """
    global _cache
    if key in _cache:
        _cache[key][0] = datetime.datetime.now()
        return _cache[key][1]
    else:
        return None


def contains(key):
    """
    Function to return the keys contained in the cache dictionary
    """
    global _cache
    return key in _cache


def size():
    """
    Function to return the current size of the cache dictionary
    """
    global _cache
    return len(_cache)


def _remove_oldest_entry():
    """
    Function to remove the oldest cached value
    """
    global _cache
    oldest = None
    for key in _cache.keys():
        if oldest is None:
            oldest = key
        elif _cache[key][0] < _cache[oldest][0]:
            oldest = key
    if oldest is not None:
        del _cache[oldest]
