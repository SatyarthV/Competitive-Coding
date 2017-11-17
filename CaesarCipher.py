#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 21:50:54 2017

@author: satyarthvaidya
"""

import sys

n = int(input().strip())
s = input().strip()
k = int(input().strip())

a = list(s)
n = len(a)

for i in range(0,n):
    o = ord(a[i])    
    if(a[i].isalpha()):
        
        if((o + k) > 90 and a[i].isupper()):
            r = (o + k) - 90
            a[i] = chr(64 + r)
            continue
        
        if((o+ k) > 122 and a[i].islower()):
            t = (o + k) - 122
            a[i] = chr(96 + t)
            continue
        
        a[i] = chr(o + k)

for i in range(0,len(a)):
    print(a[i],end="")















