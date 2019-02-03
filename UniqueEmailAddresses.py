#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 17:18:04 2019

@author: satyarthvaidya
"""

class Solution:
    def numUniqueEmails(self, emails):
        for o in range(len(emails)):
            a = emails[o]
            i = a.find('+')
            j = a.find('@')
            k = a[:i].count('.')
            a = a[:i] + a[j:]
            a = a.replace('.','',k)
            emails[o] = a
        
        return len(set(emails))