#!/usr/bin/python3
""" LIFOCaching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Defines a caching system using LIFO algorithm
    """

    def __init__(self):
        """ Initialize LIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache using LIFO algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by key
        """
        if key is not None:
            return self.cache_data.get(key)
