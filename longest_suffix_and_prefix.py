#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:35:47 2020

@author: root
"""

def find_pre_suf(s):
    l =len(s);
    
    for i in range(l//2 ,0 , -1):
        prefix = s[0:i]
        suffix = s[l-i:l]
        if prefix==suffix:
            return i;
    return 0;

print(find_pre_suf("aabcdaabc"))