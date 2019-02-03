#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 18:39:09 2019

@author: satyarthvaidya
"""

class Solution:
    def sortedSquares(self, A):
        for j in range(len(A)):
            if(A[j]<0):
                A[j] *= -1
            A[j] = A[j]*A[j]
        A.sort()
        return(A)
