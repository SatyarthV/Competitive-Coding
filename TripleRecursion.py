#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:50:49 2017

@author: satyarthvaidya
"""

#!/bin/python3

import sys

def tripleRecursion(n, m, k):
    # Complete this function

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    tripleRecursion(n, m, k)



a = [[0] * n for _ in range(n)]
for i in range(len(a)):
    for j in range(len(a)):
        if(i == j and i == 0):
            a[i][j] = m
        elif(i == j and i != 0):
            a[i][j] = a[i-1][j-1] + k
        elif(i > j):
            a[i][j] = a[i-1][j] - 1
        else:
            a[i][j] = a[i][j-1] - 1
            

for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j],end = " ")
    print("")