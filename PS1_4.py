# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 23:23:32 2021

@author: momo
"""

#Assignment 01_4
#一个大于2的数以最少的步数到1肯定是被除以2的，基于这个想法，优先对大于2的数字除以2
def Least_moves(X):
    
    a=0
    while 101>X>1:
        if X % 2 == 0:
            X=X/2
            a=a+1   
            
        else:
            X=X-1
                
            a=a+1
    
        
    print(a)
Least_moves(5)
