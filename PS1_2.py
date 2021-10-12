# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 22:43:21 2021

@author: momo
"""
#Assignment 01_2
#采用列表的形式，达到类似于矩阵的运算效果。
M1=[]
M1.append([])
import random
a=0
while len(M1)<6:
    n = random.randint(0,50)
    if len(M1[a])<10:
        M1[a].append(n)
        
    else:
        a=a+1
        M1.append([])
        
else:
    M1.pop()
    print('M1')
    print(M1)
    
    
M2=[]
M2.append([])
import random
a=0
while len(M2)<11:
    n = random.randint(0,50)
    if len(M2[a])<5:
        M2[a].append(n)
        
    else:
        a=a+1
        M2.append([])
        
else:
    M2.pop()
    print('M2')
    print(M2)   
 
    
#M3=M1*M2
d=0
e=0
f=0
M3=[]
M3.append([])
while len(M3)<6 :
    for i in M1[d]:
        g=i*M2[e][d]
        M3[d].append(g)
        e=e+1
        if e>9 :
            e=0
            d=d+1
            M3.append([]) 
        
M3.pop()
print('M3')
print(M3)


#以下是查阅网上给出的矩阵计算简便方法。自己还不会通过这种方式运用和计算矩阵。
from numpy import *;#导入numpy的库函数
import numpy as np; #这个方式使用numpy的函数时，需要以np.开头。
M1=mat(random.randint(0,50,size=(5,10)))
print(M1)
M2=mat(random.randint(0,50,size=(10,5)))
print(M2)

M=M1*M2
print(M)
#借鉴https://zhu-group.github.io/ese5023/Assignment_01.html



