#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:57:04 2020

@author: root
"""


n,k = map(int,input().split())
arr = [int(input()) for i in range(n)]
for i in range(n):
    if arr[i]<=k:
        arr[i]=0
    elif arr[i]>k:
        break;
for i in range(n-1,-1,-1):
    if arr[i]<=k:
        arr[i]=0;
    else:
        break;
print(arr)