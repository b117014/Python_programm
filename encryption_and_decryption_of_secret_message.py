#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:15:49 2019

@author: root
"""

""" print("A=",ord("A"));  ord() method is used to retrieve ascii vale of alphabet
print("65=" , chr(65));  chr() method retreive character of numeric value that privide to chr method as argument"""

user_string = input("enter string ");
secret_string = "";

for char in user_string:
    secret_string+=str(ord(char)-23);
print("secret message : " , secret_string);
decoded_string="";
for i in range(0, len(secret_string)-1 ,2):
    char_code = secret_string[i]+secret_string[i+1];
    decoded_string +=chr(int(char_code)+23);
    
print(decoded_string)
