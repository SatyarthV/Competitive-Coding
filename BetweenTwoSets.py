#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 17:21:04 2017

@author: satyarthvaidya
"""

a,b = list(map(int,input().split()))
aa = list(map(int, input().split()))

bb = list(map(int, input().split()))

if(max(aa) > max(bb)):
    mixed = list(range(max(aa)+1))
else:
    mixed = list(range(max(bb)+1))
   

count = 0
for i in range(1,len(mixed)):
#    print(i)
    if(all(mixed[i]%x == 0 for x in aa) and all(x%mixed[i] == 0 for x in bb)):
        count += 1
print(count)