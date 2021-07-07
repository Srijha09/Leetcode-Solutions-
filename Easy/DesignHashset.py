# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 10:27:35 2021

@author: Srijhak
"""

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #We need to create buckets of lists with len 1000
        self.array = [[] for _ in range(1000)]
        

    def add(self, key: int) -> None:
        subkey = key%1000
        if not self.contains(key):
            self.array(subkey).append(key)
        

    def remove(self, key: int) -> None:
        subkey = key%1000
        if self.contains(key):
            self.array(subkey).remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        subkey = key%1000
        return key in self.array[subkey]
       


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)