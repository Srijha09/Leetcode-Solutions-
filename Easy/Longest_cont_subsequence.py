# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 10:04:11 2021

@author: Srijhak
"""

def LCS(arr):
    length = 1
    mlen = 1
    for i in range(len(arr)):
        if (arr[i-1]<arr[i]):
            length+=1
        else:
            mlen = max(length, mlen)
            length = 1
    return max(length, mlen)


        
        