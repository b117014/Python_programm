#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 23:20:16 2020

@author: root
"""

class Solution:
    def freqAlphabets(self, s: str):
        l = ""
        alp = "abcdefghi"
        alp2 = "jklmnopqrstuvwxyz"
        num = "123456789"
        num2 = ["10#","11#","12#","13#","14#","15#","16#","17#","18#","19#","20#","21#","22#","23#","24#","25#","26#"]
        print(len(alp2))
        s = s + " " + " "
        i=0;
        while i<len(s)-2:
            print(i)
            
            if( s[i+2]!="#"):
                for k in range(len(num)):
                    if(num[k]==s[i]):
                        l=l+alp[k];
                        i=i+1;
                        break
                print(l)
            else:
                for j in range(len(num2)):
                    m = s[i]+s[i+1]+s[i+2];
                    i = i+2;
                    if(num2[j]==m):
                        l = l+alp2[j];
                        break
                print(l)
        return l;
               
              
        
        
l = Solution()
l.freqAlphabets("10#11#12")