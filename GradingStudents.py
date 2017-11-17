#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 00:14:40 2017

@author: satyarthvaidya
"""

import sys

def solve(grades):
    # Complete this function
    for i in range(0,len(grades)):
#        if(grades[i] <
        if(5 - (grades[i] % 5) <= 2 and grades[i] >= 38):
            grades[i] = grades[i] + 5 - (grades[i]%5)
            
            
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))

