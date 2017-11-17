#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 21:49:07 2017

@author: satyarthvaidya
"""

string = "AABCAAADA"
k = 3

for i in range(0,len(string),k):
    foo = string[i:i+3]
    print(''.join(sorted(set(foo), key=foo.index)))

























