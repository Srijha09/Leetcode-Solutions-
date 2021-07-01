# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 22:11:54 2021

@author: Srijhak
"""


def maxSubArray(nums):
    total = 0
    res = float('-inf')
    
    for i in range(len(nums)):
        total += nums[i]
        res = max(res, total)
        
        if total < 0:
            total = 0
    return res

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))