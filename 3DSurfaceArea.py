#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 18:06:53 2017
@author: satyarthvaidya
"""
#!/bin/python3
import sys
def surfaceArea(A):
    # Complete this function
    su = 0 
    for i in range(len(A)):
        su = su + max(A[i])
    
        
    rhsv_max = 0
    for i in range(len(A)):
        temp = 0
        for j in range(len(A)):
            if(A[j][i] > temp):
                temp = A[j][i]
    #            print(temp)
        rhsv_max += temp
    
    hidden = 0
    for i in range(len(A)-2):
        for j in range(len(A)-2):
            if(A[j][i+2] == A[j][i] and A[j][i+2] - A[j][i+1] >= 0):
                hidden += 1
    
    hidden_rhsv = 0
    for i in range(len(A)):
        for j in range(len(A)-2):
            if(A[j+2][i] >= A[j][i] and A[j+2][i] > A[j+1][i]):
                hidden_rhsv += A[j+2][i] - A[j+1][i]
    
    ans = (su + rhsv_max + hidden + H*W + hidden_rhsv)*2
    return ans

if __name__ == "__main__":
    H, W = input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = []
    for A_i in range(H):
       A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
       A.append(A_t)
    result = surfaceArea(A)
    print(result)

#fv_max = 0
#for i in range(0,len(A)):
#    fv_max = fv_max + max(A[i])
#    
#rhsv_max = 0
#a = np.array(A,dtype = int)
#
#
##rhsv_max
#sum(a.max(axis=0))
#
#fv_max
#sum(a.max(axis=1))
#    
##top_max
#np.count_nonzero(a) 
#    
#print((sum(a.max(axis=0)) + sum(a.max(axis=1)) + np.count_nonzero(a)))*2)    
#    
#count = 0
#for i in range(0,len(a)-2):
#    for j in range(0,len(a)):
#        if(a[i+2][j] == a[i][j] and a[i+2][j] -a[i+1][j] > 0):
#            count += 1    
#
#ans = (sum(a.max(axis=0)) + sum(a.max(axis=1)) + np.count_nonzero(a) + count) * 2
#    
    
#fv_max   
su = 0 
for i in range(len(A)):
    su = su + max(A[i])

    
rhsv_max = 0
for i in range(len(A)):
    temp = 0
    for j in range(len(A)):
        if(A[j][i] > temp):
            temp = A[j][i]
#            print(temp)
    rhsv_max += temp

hidden = 0
for i in range(len(A)-2):
    for j in range(len(A)-2):
        if(A[j][i+2] == A[j][i] and A[j][i+2] - A[j][i+1] >= 0):
            hidden += 1

hidden_rhsv = 0
for i in range(len(A)):
    for j in range(len(A)-2):
        if(A[j+2][i] >= A[j][i] and A[j+2][i] > A[j+1][i]):
            hidden_rhsv += A[j+2][i] - A[j+1][i]

ans = (su + rhsv_max + hidden + H*W + hidden_rhsv)*2
return ans


count = 0
for j in range(0,len(A)): 
    for i in range(0,len(A)):
        hold = A[len(A)-1][j] > A[len(A)-2][j]
        if(A[i][j] == A[len(A)-1][j] and hold):
            count += 1














   
    
    
