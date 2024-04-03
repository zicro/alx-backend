#!/usr/bin/python3
""" BasicCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Defines a basic caching system
    """

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by key
        """
        if key is not None:
            return self.cache_data.get(key)
