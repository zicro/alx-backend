#!/usr/bin/python3
""" FIFOCaching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Defines a caching system using FIFO algorithm
    """

    def __init__(self):
        """ Initialize FIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache using FIFO algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key, _ = next(iter(self.cache_data.items()))
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by key
        """
        if key is not None:
            return self.cache_data.get(key)
