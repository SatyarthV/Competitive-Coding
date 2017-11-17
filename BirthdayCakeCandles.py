#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 23:26:30 2017

@author: satyarthvaidya
"""

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    ar.sort()
    return ar.count(ar[-1])

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)