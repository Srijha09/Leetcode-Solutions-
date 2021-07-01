# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once).

# Return the sum of lengths of all good strings in words.

def countCharacters(words, char):
    count = 0
    for i in words:
        flag = True
        for j in i:
            if words.count(j)>char.count(j):
                flag = False
                break
        if flag:
            count += len(i)
        
    return count