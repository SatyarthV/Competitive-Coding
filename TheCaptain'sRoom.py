#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 13:27:08 2017

@author: satyarthvaidya
"""



set0 = set(room[0:6])



k = int(input())
room = list(map(int,input().split()))
if(len(room)%2 == 0):
    n = int(len(room)/2)
    set1 = set(room[:n])
    set2 = set(room[n:])
#    print(set1)
#    print(set2)
    a = list((set1.difference(set2)).union(set2.difference(set1)))
    print(a[0])
else:
    n = int((len(room)-1)/2)
    set1 = set(room[:n])
    set2 = set(room[n:])
#    print(set1)
#    print(set2)
#    print((set1.difference(set2)).union(set2.difference(set1)))
    a = list((set1.difference(set2)).union(set2.difference(set1))) 
    print(a[0])













