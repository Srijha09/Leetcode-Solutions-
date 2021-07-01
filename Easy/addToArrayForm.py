# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 22:30:53 2021

@author: Srijhak
"""

#  Thought Process
# given a num as an array and k as an integer
# Convert the num list to str
# Add the str(num) with k
# convert it back to a list of integers

def addToArrayForm(lis, k):
    num = int(''.join(i) for i in lis)
    res = list(str(num)+k)
    res = list(map(str,int))
    return res

lis = [1,3,5,6]
k = 67
print(addToArrayForm(lis, k))