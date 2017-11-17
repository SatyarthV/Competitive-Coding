#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 08:59:13 2017

@author: satyarthvaidya
"""

A = set(input().split()) 

count  = []
a = int(input())
for i in range(0,a):
    B = set(input().split())
    if(len(A.difference(B)) >= 1 and len(B.difference(A)) == 0):
        count.append(1)
    else:
        print("False")
        break

if(sum(count) == a):    
    print("True")



#
#if(len(A.difference(B)) == 0):
#
#
#
#






  















