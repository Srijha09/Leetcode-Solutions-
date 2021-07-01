# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 22:38:34 2021

@author: Srijhak
"""

def arrayPairSum(nums):
    nums.sort()
    i=0
    sum=0
    while i < len(nums):
        sum+=i
        i+=2
    return sum


nums = [1,6,7,8,4,2,9]
print(arrayPairSum(nums))