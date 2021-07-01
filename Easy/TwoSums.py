# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 21:34:54 2021

@author: Srijhak
"""

#Brute Force

# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i]+nums[j]==target:
#                 return i,j


#O(N) solution: first create a dictionary, add target-nums to dict, check if the complement present in dictionary

def twoSum(nums,target):
    dic = {}
    
    for i in range(len(nums)):
        if target-nums[i] in dic:
            return [dic[target-nums[i]],i]
        else:
            dic[nums[i]]=i


nums = [1,3,4,5]
target = 7

print(twoSum(nums, target))
