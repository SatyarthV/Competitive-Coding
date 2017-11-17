#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 12:43:42 2017

@author: satyarthvaidya
"""

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))

unique = list(set(ar))

co =[]

for i in range(0,len(unique)):
    co.append(ar.count(unique[i]))
    
for i in range(0,len(co)):
    co[i] = int((co[i])/2)

print(sum(co))