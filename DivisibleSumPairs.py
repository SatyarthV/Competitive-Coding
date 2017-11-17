#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 11:32:37 2017

@author: satyarthvaidya
"""

    
############################
#DIVISIBLE SUM PAIRS


import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

count = 0
for i in range(0,n-1):
    for j in range(i+1,n):
#        print(str(a[i]) + " " + str(a[j]))
        if((a[i]+a[j])%k == 0):
            count += 1
            
print(count)
