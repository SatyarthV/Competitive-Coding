#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 22:52:27 2017

@author: satyarthvaidya
"""
import sys

def migratoryBirds(n, ar):
    count = [0]*6
    for t in ar:
        count[t] += 1
    return count.index(max(count))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
