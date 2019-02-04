#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 18:10:37 2019

@author: satyarthvaidya
"""

class Solution:
    
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        a=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        lis = []
        for j in range(0,len(words)):
            c = ""
            for i in range(0,len(words[j])):
                b = ord(words[j][i]) - 97
                c = c + a[b]

            lis.append(c)
        
        return(len(set(lis)))
        