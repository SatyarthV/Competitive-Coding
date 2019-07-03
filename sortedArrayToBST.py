#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 09:56:07 2019

@author: satyarthvaidya
"""

def sortedArrayToBST(nums):
    
    if not nums: 
        return None
    mid = (len(nums)) // 2
    root = TreeNode(nums[mid]) 
    root.left = sortedArrayToBST(nums[:mid]) 
    root.right = sortedArrayToBST(nums[mid+1:]) 
    return root 

lis = [-10,-3,0,5,9]

a = sortedArrayToBST(lis)
