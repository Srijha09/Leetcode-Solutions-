# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:11:52 2021

@author: Srijhak
"""

def HappyNumbers(num):
    
    def sqsum(num):
        sq  = 0
        while num > 0:
    
            r = num % 10
            sq = sq + r*r
            num =  num//10
        return sq
    
    visited = set()
    
    while sqsum(num) not in visited:
        sums = sqsum(num)
        print(sums)
        if sums == 1:
            return True
        else:
            visited.add(sqsum(num))
            num = sums
    return False
    
nums = 19
print(HappyNumbers(nums))