#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:56:12 2017

@author: satyarthvaidya
"""

#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)


bill = 0
for i in range(0,len(ar)):
    if(i != k):
        bill = bill + ar[i]

if(b - (bill/2) == 0):
    print("Bon Appetit")
else:
    print(int(b - (bill/2)))
    
    




































