# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:11:52 2021

@author: Srijhak
"""
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Thought process
# Traverse through the LL store the values in a hash, if already visited return true
#But this has a time complexity of O(n) and space of O(n) we need O(1)

# Solution 2
# We have two pointers : one having two jumps and other pointer having one jump
# If they eventually meet there is a cycle

def hasCycle(head):
    slow = fast = head
    
    while slow and fast and fast:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False
