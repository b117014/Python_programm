#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:28:14 2020

@author: root
"""

for _ in range(int(input())):
    st = input();
    st = list(st)
   
    bl=0
    rd=0
    for bal in st:
        if bal=='b':
            bl+=1
        else:
            rd+=1
    
    if bl<=rd:
        print(bl)
    else:
        print(rd)
        
    