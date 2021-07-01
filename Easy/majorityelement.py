# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 10:12:36 2021

@author: Srijhak
"""

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


def majorityElement(n):
    return sorted(n)[len(n//2)]

 