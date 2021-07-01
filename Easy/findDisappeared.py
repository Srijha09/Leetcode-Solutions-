# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 09:57:23 2021

@author: Srijhak
"""

def findDisappearedNumbers(n):
    N = set()
    for i in range(1, len(n)):
        if i not in N:
            return i