# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 09:53:11 2021

@author: Srijhak
"""

def numberofplants(fbed,n):
    count = 0
    for i in range(len(fbed)):
        if (fbed[i]==0 and (i==0 or fbed[i-1]==0) and (i==len(fbed or fbed[i+1]==0))):
            fbed[i]=1
            count+=1
    return count >= n
            
    