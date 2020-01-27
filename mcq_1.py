#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:52:41 2020

@author: root
"""

class ClassA:
    def _init_(self,val):
        self.vals = val
    def obj_A(self):
        return 10 + self.vals

class ClassB:
    def _init_(self,num):
        self.nums = num
    def obj_B(self,obj):
        return obj.obj_A() + self.nums
    
obj1 = ClassA(20)
obj2 = ClassB(30)
print(obj2.obj_B(obj1))