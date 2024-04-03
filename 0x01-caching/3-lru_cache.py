#!/usr/bin/python3
""" LRUCaching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Defines a caching system using LRU algorithm
    """

    def __init__(self):
        """ Initialize LRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache using LRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))

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
