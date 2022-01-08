"""
Test script to verify the cache.py module is working correctly
"""

import random
import string
import cache

def random_string(length):
    """
    Function to generate a string of random lower and uppercase ascii
    characters with a given length.
    """
    str = ''
    for str in range(length):
        str = str + random.choice(string.ascii_letters)
    return str


cache.init()


for n in range(1000):
    while True:
        key = random_string(20)
        if cache.contains(key):
            continue
        else:
            break
    value = random_string(20)
    cache.set(key, value)
    print("After {} iterations, cache has {} entries".format(n+1, cache.size()))
