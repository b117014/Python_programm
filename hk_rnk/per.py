#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 01:07:00 2020

@author: root
"""

from itertools import permutations

perm = permutations([1,2,3,4], 2)

print(list(perm))