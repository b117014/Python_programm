#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:47:52 2020

@author: root
"""

r1 = 26;

r2 = int(input("enter number to find multiplicative inverse"))
t1 = 0;
t2 = 1;
temp = r2
while(r2>0):
    q = int(r1/r2);
    
    r = r1 - q*r2
    r1 = r2 
    r2 = r;
    
    t = t1 - q*t2;
    t1 = t2 
    t2 = t
    

if r1==1:
    print("inverse of " ,temp ," is ", t1 )
else:
    print("inverse doesn't exist");
