#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 22:25:19 2017

@author: satyarthvaidya
"""

m = int(input())
mset = list(map(int, input().split()))

n = int(input())
nset = list(map(int, input().split()))

setm = set(mset)
setn = set(nset)

a = (setm.difference(setn)).union(setn.difference(setm))

for i in sorted(a):
    print(i)





























