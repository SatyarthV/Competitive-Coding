#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 11:35:03 2017

@author: satyarthvaidya
"""

import sys

def solve(n, s, d, m):
    # Complete this function

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)




count = 0
for i in range(0,len(s)-m+1):
    su = 0
    for j in range(i,i+m):
        su = su + s[j]
    if(su == d):
        count += 1

print(count)


































