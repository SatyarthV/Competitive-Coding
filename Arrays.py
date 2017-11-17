#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:45:05 2017

@author: satyarthvaidya
"""
import numpy as np
arr = input().strip().split(' ')
a = np.array(arr,float)
b = []
for i in range(0,len(a)):
    b.append(a[len(a)-i-1])

final = np.array(b)
return final