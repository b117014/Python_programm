#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:05:38 2020

@author: root
"""
import re;
text = 'From: hello: 2 I am goingm 19 to start running'

check = re.findall('^F.+?:',text)
print(check)