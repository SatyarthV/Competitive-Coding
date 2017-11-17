#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 18:44:27 2017

@author: satyarthvaidya
"""

string = "BANANA"
kevin_score = 0
stuart_score = 0

for i in range(0,len(string)):
    if(string[i][0] == 'A' or string[i][0] == 'E' or string[i][0] == 'I' or string[i][0] == 'O' or string[i][0] == 'U' ):
        kevin_score = kevin_score +  len(string) - i
    else:
        stuart_score = stuart_score +  len(string) - i


if(kevin_score == stuart_score):
    print("Draw")
else:
    if(kevin_score > stuart_score):
        print("Kevin " + str(kevin_score))
    else:
        print("Stuart " + str(stuart_score))




