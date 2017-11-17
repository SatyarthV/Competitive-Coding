#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:42:54 2017

@author: satyarthvaidya
"""

import textwrap


s = "abcdefghijklmnopqrstuvxyzjkmo"
p = []   
    
for i in range(0,len(s),4):
    p.append(s[0:i])

t=[]

for i in range(1,len(p)):
    t.append(p[i].replace(p[i-1],''))
    
for i in range(0,len(t)):
    print(t[i])
    
    
print(s.replace(p[len(p)-1],''))


def wrap(string, max_width):
    s = textwrap.fill(string,max_width)
    for i in range(0,len(s)):
        print(s[i])
    return


def wrap1(string, max_width):
    a = textwrap.wrap(string,max_width)
    return