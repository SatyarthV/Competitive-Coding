#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 12:44:00 2017

@author: satyarthvaidya
"""

e = int(input())
engn = list(map(int,input().split()))

f = int(input())
fren = list(map(int,input().split()))

engn =set(engn)
fren = set(fren)

print(len(engn.symmetric_difference(fren)))
