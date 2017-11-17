#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:29:24 2017

@author: satyarthvaidya
"""

inp = input()
su = []

for i in range(1,len(inp)):
    if(inp[0:i] == inp[-i:]):
        su.append(len(inp[0:i]))
        
print(max(su))






