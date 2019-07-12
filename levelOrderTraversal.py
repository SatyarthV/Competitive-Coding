#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 19:02:02 2019

@author: satyarthvaidya
"""
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
def levelOrderBottom(root):
    
    stack = [(root,0)]
    res = []
    while stack:
        print("HI")
        node, level = stack.pop()
        if node:
            if(len(res) < (level + 1)):
                res.insert(0,[])
            res[-(level+1)].append(node.val)
            stack.append((node.right,level+1))
            stack.append((node.left,level+1))
    return res

   
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

root.left = node1
root.right = node2
node1.left = node4
node1.right = node5
node5.right = node6

a = levelOrderBottom(root)
