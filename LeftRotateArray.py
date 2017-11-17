#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 16:58:29 2017

@author: satyarthvaidya
"""


n,d = input().strip().split(' ')
arr=input().strip().split(' ')

d=int(d)

temp = arr[:d]

arr=arr[d:] + temp
for i in range(0,len(arr)):
    print(arr[i],end=" ")
























