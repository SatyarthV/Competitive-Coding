#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:00:14 2017

@author: satyarthvaidya
"""

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]



for i in range(0,len(apple)):
    apple[i] = apple[i] + a

for i in range(0,len(orange)):
    orange[i] = orange[i] + b
    
count_apple = 0

for i in range(0,len(apple)):
    if(apple[i] >= s and apple[i] <= t):
        count_apple += 1
        

count_orange = 0

for i in range(0,len(orange)):
    if(orange[i] >= s and orange[i] <= t):
        count_orange += 1
        
print(count_apple)
print(count_orange)

