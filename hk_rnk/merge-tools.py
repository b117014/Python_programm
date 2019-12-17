#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:05:14 2019

@author: root
"""

def remove(arr):
    final_list=[]
    for part in arr:
        if part not in final_list:
            final_list.append(part)
    return final_list

strr = input()
k = int(input());
l = len(strr)
n = int(l/k);
for i in zip(*[iter(strr)]*n):
    d= []
    for c in i:
        if c not in d:
            d.append(c)
    print("".join(d))
        
    
