#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 01:11:27 2020

@author: root
"""

for _ in range(int(input())):
    n = int(input())
    if n%4==1:
        print("ALICE")
    else:
        print("BOB")