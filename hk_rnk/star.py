#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:29:10 2020

@author: root
"""


from itertools import combinations;

n = int(input());
arr = list(map(str,input().split()));

k = int(input())

count = 0
perm = combinations(arr,k)
perm_len = len(list(perm))

for temp in list(combinations(arr,k)):
    print(temp)
    if 'a' in temp:
        count+=1;

print(count/perm_len)
