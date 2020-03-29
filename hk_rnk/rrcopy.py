#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:30:51 2020

@author: root
"""

for _ in range(int(input())):
    n = int(input())
    arr = set(map(int,input().split()))
    temp_arr=[]
    for val in arr:
        if val not in temp_arr:
            temp_arr.append(val)
    print(len(temp_arr))