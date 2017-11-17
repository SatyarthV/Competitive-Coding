#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:44:08 2017

@author: satyarthvaidya
"""

n,m = map(int,input().split())

outcome = 0
arr = input().split()
A = input().split()
B = input().split()

for i in arr:
  if (i in A):
    outcome+=1
  if (i in B):
    outcome-=1
    
print(outcome)
