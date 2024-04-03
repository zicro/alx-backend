#!/usr/bin/python3
""" MRUCaching module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Defines a caching system using MRU algorithm
    """

    def __init__(self):
        """ Initialize MRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache using MRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item from the cache by key
        """
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        else:
            return None
