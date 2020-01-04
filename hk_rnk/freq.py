#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 15:33:04 2019

@author: root
"""
def count(string):
    d = {};
    ct=0
    for part in string:
        if part in d:            
            d[part]+=1;
        elif part not in d:
            d[part]=1
            
    for i in d:
        ct+=1;
    print(ct)
    for part in d:
        print(d[part] , end=" ")

n = int(input())
string=[]
for i in range(n):
   string.append(input())

count(string)
    