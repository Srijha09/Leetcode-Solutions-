# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 23:17:21 2021

@author: Srijhak
"""

def merge(nums1, m, nums2, n):
    i=j=k=0
    
    
    while i<=m and j<=n:
        if nums1[i]<nums2[j]:
            nums1[k]=nums1[i]
            i+=1
            k+=1
        else:
            nums1[k]=nums2[j]
            j+=1
            k+=1
        
        if j<=m-1:
            nums1[k:]=nums2[j:]
        
        return nums1
            