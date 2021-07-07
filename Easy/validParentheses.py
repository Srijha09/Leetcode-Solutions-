# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 12:24:40 2021

@author: Srijhak
"""

def isValid(s):
    stack = []
    lookup = {")":"(","]":"[","}":"{"}
    
    for paran in s:
        if paran in lookup.values():
            stack.append(paran)
        elif stack and stack[-1]==lookup[paran]:
            stack.pop()
        else:
            return False
    return stack==[]


s = "[]}"
print(isValid(s))