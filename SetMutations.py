#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 12:51:42 2017

@author: satyarthvaidya
"""
n = int(input())
numbers = list(map(int,input().split()))

numbers = set(numbers)

iterations = int(input())
for i in range(0,iterations):
    oper = input().split()
    set2 = list(map(int,input().split()))
    set2 = set(set2)
    
    if(oper[0] == 'difference_update'):
        numbers.difference_update(set2)
        
    elif(oper[0] == 'intersection_update'):
        numbers.intersection_update(set2)
         
    elif(oper[0] == 'update'):
         numbers.update(set2)
         
    elif(oper[0] == 'symmetric_difference_update'):
         numbers.symmetric_difference_update(set2)
         
    

print(sum(numbers))




