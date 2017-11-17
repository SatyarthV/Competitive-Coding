#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 19:06:26 2017

@author: satyarthvaidya
"""
sy = input()
p,d,m,s = (int(x) for x in sy.split())

mini = s-p

while True:
    mini = s-p
    p = p-d
    if(mini == m):
        mini = mini - m
    


import sys

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    lis = []
#    sum = 0
#    for j in range(0,1000):
    while True:
        if(p>m):    
            lis.append(p)
            p = p-d
        else:
            lis.append(m)
        
#        su = sum(lis)
        if(sum(lis) >= s):
            break
        
#    for i in range(0,1000):
#        sum = sum + lis[i]
#        print(sum)
#        if(sum >= s):
#            break
#    print(sum)
#    print(lis)
#    return i
    return len(lis)-1
    
    
    
    

if __name__ == "__main__":
    p, d, m, s = input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print(answer)






while True:
     do_something()
     if condition():
        break











