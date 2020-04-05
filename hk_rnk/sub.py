#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:20:52 2020

@author: root
"""

for _ in range(int(input())):
    n = int(input())
    s=[]
    p=[]
    for i in range(n):
        a,b = map(int,input().split());
        s.append(a)
        p.append(b)
    
    d=dict()
    sum_=0
    print(s)
    for i,j in s,p:
        d[i]=j
    arr=[]
    for i,j in d.items():
        if i<9 and i not in arr:
            arr.append(i)
            sum_+=j
    print(sum_)
            
            
                