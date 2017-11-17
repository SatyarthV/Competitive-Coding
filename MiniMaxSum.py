#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 23:34:54 2017

@author: satyarthvaidya
"""
import sys

arr = list(map(int, input().strip().split(' ')))
arr.sort()
print(str(sum(arr)-arr[-1]) + " " + str(sum(arr)-arr[0]))