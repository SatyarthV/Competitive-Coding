#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 17:58:21 2017

@author: satyarthvaidya
"""
n= int(input())
li=[]

for i in range(0,n):
    a = input()
    li.append(a.split(" "))
    
dic={}
for i in range(0,n):
    dic[str(li[i][0])] = int(li[i][1])
    
while(input != ''):
    a = input()
    if(a not in dic):
        print("Not Found")
    else:
        print(a + "=" + str(dic[a]))
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    