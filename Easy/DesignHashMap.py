# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 11:53:29 2021

@author: Srijhak
"""

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hm = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hm[key]=value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.hm:
            return self.hm[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.hm:
            del self.hm[key]