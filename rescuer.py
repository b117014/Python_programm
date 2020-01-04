#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 23:57:21 2019

@author: root
"""
import math
n = int(input())

for i in range(0,n):
    l = list(map(int,input().split()))
    if(l[0]-l[2] == 0):
        d1 = math.sqrt(l[1]*l[1])
        d2 = math.sqrt(l[3]*l[3])
        t1 = d1/l[4];
        t2 = d2/l[5];
        r = t1+t2
        print('%.5f'%r)
    else:
        m = (l[3]-l[1])/(l[2]-l[0])
        print(m)
        c = l[1] - m*l[0]
        print(c)
        x = -c/m
        print(x)
        d3 = math.sqrt(math.pow((l[0]-x),2)+(l[1]*l[1]))
        d4 = math.sqrt(math.pow((l[2]-x),2)+(l[3]*l[3]))
        t3 = d3/l[4]
        t4 = d4/l[5]
        r2 = t3+t4
        print('%.5f'%r2)