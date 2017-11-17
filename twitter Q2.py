#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 18:56:11 2017

@author: satyarthvaidya
"""

import datetime
import time

test = input()
a = test.split(',')
a[1] = a[1].replace(" ","")
date1 = a[0]
date2 = a[1]

inp = input()       
parentlist=[]
i = 0
h=[[]]
parentlist.append(inp.split())
while inp != "":        
    inp =input() 
    parentlist.append(inp.split())

j = [[] for _ in range(0,len(parentlist)-1)]          

for i in range(0,len(parentlist)-1):
    a = parentlist[i][0][0:10]
    b = parentlist[i][0][11:-3]
    c = parentlist[i][0][-3:]
    j[i].append(a)
    j[i].append(b)
    j[i].append(c)

newdate1 = time.strptime(date1, "%Y-%m")
newdate2 = time.strptime(date2, "%Y-%m")

for i in range(0,len(j)):
    j[i][0] = "-".join(j[i][0].split("-", 2)[:2])

l=[]

for i in range(0,len(j)):
    if(time.strptime(j[i][0],"%Y-%m") >= newdate1 and time.strptime(j[i][0],"%Y-%m") <= newdate2):
        l.append(j[i][0])

l=sorted(l, key=lambda x: datetime.datetime.strptime(x, '%Y-%m'))

dic = {}
for i in range(0,len(l)):
    dic[l[i]] = {}

for i in range(0,len(l)):
    for k in range(0,len(j)):
        if(str(j[k][0]).find(str(l[i])) == 0):
            dic[l[i]][j[k][1]] = j[k][2]
print(dic)

#inputs

#test = input()
#a = test.split(',')
#newdate1 = a[0]
#newdate2 = a[1]
#
#inp = input()       
#parentlist=[]
#i = 0
#h=[[]]
#parentlist.append(inp.split())
#while inp != "":        
#    inp =input() 
#    parentlist.append(inp.split())
#
#h = [[] for _ in range(0,len(parentlist)-1)]          
#
#for i in range(0,len(parentlist)-1):
#    a = parentlist[i][0][0:10]
#    b = parentlist[i][0][11:-3]
#    c = parentlist[i][0][-2:]
#    h[i].append(a)
#    h[i].append(b)
#    h[i].append(c)
       
#    2015-08-15,clicks,635
#    2016-11-07,impressions,245
#   
#j = [[2015-08-15','clicks',635],
#     [2016-03-24','app_installs',683],
#     [2015-04-05','favourites',763],
#     [2016-01-22','favourites',788],
#     [2015-12-26','clicks',525],
#     [2016-06-03','retweets',101],
#     [2015-12-02','app_installs',982],
#     [2016-09-17','app_installs',770],
#     [2015-11-07','impressions',245],
#     [2016-10-16','impressions',567]
#     ]
