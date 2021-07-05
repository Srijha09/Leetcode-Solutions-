# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:23:58 2021

@author: Srijhak
"""

def countprimes(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    primes = [1]*n #create a list consisting of all true
    primes[0]=0
    primes[1]=0
    
    i = 2
    while i<n:
        tmp = i
        if primes[i]:
            tmp+=i
            while tmp<n:
                primes[tmp]=0
                tmp+=i
        i+=1
        
    return(sum(primes))

num = 10
print(countprimes(num))