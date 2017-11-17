#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 11:33:09 2017

@author: satyarthvaidya
"""

n = int(input())
numbers = list(map(int,input().split()))

numbers = set(numbers)

iterations = int(input())
for i in range(0,iterations):
    oper = input().split()
    if(oper[0] == 'pop'):
        numbers.pop()
    elif(oper[0] == 'remove'):
        numbers.remove(int(oper[1]))
    else:
        numbers.discard(int(oper[1]))

print(sum(numbers))



























































