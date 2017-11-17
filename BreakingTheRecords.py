#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 21:42:54 2017

@author: satyarthvaidya
"""

min_score = s[0]
count = 0
max_score = s[0]
max_count = 0

for i in range(0,len(s)):
    if(s[i] < min_score):
        count += 1
        min_score = s[i]
#        print(i)
        
    if(s[i] > max_score):
        max_score = s[i]
        max_count += 1
#        print(i)
        
return max_count,count



count = 0
for i in range(0,len(s)-m+1):
    su = 0
    for j in range(i,i+m):
        su = su + s[j]
    if(su == d):
        count += 1

print(count)



