#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:35:15 2019

@author: root
"""
from itertools import groupby

s = input()


for k, g in groupby(s):  """ k is key and g group groupby make group of same value in array or string """

    print("({},{})".format(len(list(g)),k), end=" ")
    