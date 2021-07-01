# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 22:18:18 2021

@author: Srijhak
"""

def isOneBitCharacter(bits):
    for i in range(len(bits)):
        if bits[i]==1:
            i+=2
        elif bits[i]==0:
            i+=1
        return i == len(bits)-1

bits = [1,1,0]
print(isOneBitCharacter(bits))
