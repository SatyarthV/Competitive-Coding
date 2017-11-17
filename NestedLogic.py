#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 01:07:52 2017

@author: satyarthvaidya
"""
from datetime import datetime
import time
import sys

act1 = input()
due1 = input()

act = act1.split(' ')
due = due1.split(' ')

if(int(act[2]) == 12):
    print(10000)
    sys.exit(0)

if(int(act[2]) == 1):
    print(0)
    sys.exit(0)

act_date = time.strptime(act1,"%d %m %Y")
due_date = time.strptime(due1,"%d %m %Y")

if(act_date < due_date):
    print(0)
else:
    if(int(due[2]) < int(act[2])):
        print(10000)
    
    elif(int(due[1]) < int(act[1])):
        n = int(act[1]) - int(due[1])
        print(500 * abs(n))
    
    elif(int(due[0]) < int(act[0])):
        d = int(due[0]) - int(act[0])
        print(15*abs(d))
    
    else:
        print(0)
    





















