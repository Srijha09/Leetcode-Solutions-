# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:11:53 2021

@author: Srijhak
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#USING EXTRA SPACE
# def getIntersectnode(headA, headB):
#     visited = set()
#     curA, curB = headA, headB
    
#     while curA:
#         visited.add(curA)
#         curA.next
    
#     while curB:
#         if curB in visited:
#             return curB
#         curB = curB.next
#     return None

def getIntersectionNode(headA, headB):
    curA, curB = headA, headB
    a, b = 0, 0
    while curA:
        a+=1
        curA = curA.next
    while curB:
        b+=1
        curB = curB.next
    
    while a>b:
        curL = headA
        diff = a-b
        curS = headB
    
    while b>a:
        curL = headB
        diff = b-a
        curS = headA
    
    while curL!=curS:
        curL = curL.next
        curS = curS.next
    
    return curL


    
        