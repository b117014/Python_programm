#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 22:07:40 2020

@author: root
"""

def solve(s):
    s = s.split(" ");
    p = "";
    for temp in s:
        temp = temp.replace(temp[0],temp[0].upper())
        p =   p+temp + " "
    
    p = p[:-1];
    return p;
        
print(solve("hello world lol"))