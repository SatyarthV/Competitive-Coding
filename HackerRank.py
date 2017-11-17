#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:26:29 2017

@author: satyarthvaidya
"""


#TEXT WRAP CODE BELOW
import textwrap

string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4

a = textwrap.wrap(string,max_width)
for i in range(0,len(a)):
    print(a[i])

print(textwrap.fill(string,4))

m = len(string)/max_width
for i in range(0,len(string),max_width):
    print(string[i:i+max_width])

###########################


#STRING FORMATING

s = 6
reps = s/2
li = []

for i in range(0,int(reps)):
    n = int(s/2)
    r = s%2
    s = n
    #print("NUMBER " + str(n)) 
    li.append(r)
    print("REMAINDER " + str(r))



for i in range(0,len(li)):
    print(round(li[len(li)-1-i]),end = "")
t
import math
for s in range(0,8):
    if(s == 0):
        print(0)
        continue
    if(s == 1):
        print(1)
        continue
    l = []
    s = 5
    
    for i in range(0,int(s/2)):
    #   print(math.floor(n))
        n = math.floor(s/2)
        r = s%2
        s = n
    #   print(r)
        l.append(r)
        
    for i in reversed(l):
        print(l[i],end="")
    print("\n")
        
##################################
##BITWISE AND


import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]

    li=[]
    for i in range(1,n):
        for j in range(i+1,n+1):
            c = i & j
            if(c < k):
                li.append(c)
    
    li.sort(reverse=True)
    print(li[0])











