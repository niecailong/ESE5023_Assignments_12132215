# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 23:01:00 2021

@author: momo
"""
#Assignment 01_3

pascal=[[1],[1,1],[]]

def Pascal_triangle(x):
    pascal=[[1],[1,1],[]]
    for a in range(0,x):
        
        a=len(pascal)-1
        c=0
        for p in range(0,len(pascal[a-1])+1):
            
            if len(pascal[a])<1 or len(pascal[a])>a-1:
                b=1
                pascal[a].append(b)
            
        
            else:
                b=pascal[a-1][c-1]+pascal[a-1][c]
                
                pascal[a].append(b)
               
            c=c+1
        
        
        pascal.append([])
    
    pascal.pop()
    print(a-1)        
    print(pascal)

Pascal_triangle(100) 
Pascal_triangle(200)
