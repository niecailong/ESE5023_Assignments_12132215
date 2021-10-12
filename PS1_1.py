# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 22:35:01 2021

@author: momo
"""
#Assignment 01_1
def ABC(a,b,c):
    if a>b:
        if b>c:
            return(a,b,c)
        else:
            if a>c:
                return(a,c,b)
            else:
                return(c,a,b)
    else:
        if b>c:
            print("ture")
        else:
            return(c,b,a)

ABC(1,3,2)            