#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:09:10 2020

@author: root
"""

def gcd(a,b):
    if b==0:
        return a;
    else:
        return gcd(b,a%b)
    

for _ in range(int(input())):
    a,b = map(int,input().split())
    print(gcd(a,b))

    