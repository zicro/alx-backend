#!/usr/bin/python3
""" LFUCaching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Defines a caching system using LFU algorithm
    """

    def __init__(self):
        """ Initialize LFUCache
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item to the cache using LFU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items()
                            if v == min_freq]

                if len(lfu_keys) > 1:
                    lru_key = min(lfu_keys, key=lambda k: self.order.index(k))
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    print("DISCARD: {}".format(lru_key))
                else:
                    lfu_key = lfu_keys[0]
                    del self.cache_data[lfu_key]
                    del self.frequency[lfu_key]
                    print("DISCARD: {}".format(lfu_key))

            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        """ Get an item from the cache by key
        """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        else:
            return None
