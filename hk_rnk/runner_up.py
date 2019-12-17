#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:45:15 2019

@author: root
"""
def Remove(duplicate):
    final_list = [];
    for t in duplicate:
        if t not in final_list:
            final_list.append(t)
    return final_list;
        

n = int(input());
arr = list(map(int, input().split()))

arr.sort();
arr = Remove(arr);

print(arr[len(arr)-2]);