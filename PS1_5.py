# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 21:44:14 2021

@author: momo
"""
#Assignment 01_5
#自己理清楚了是一种3**8次方的排列组合，但是自身能力有限无法实现数字组合成两位数。只能做到每个数字和‘+’和‘-’的排列组合。

def expression(y):
    n=[1,2,3,4,5,6,7,8,9]
    m=[]
    v=[]
    f=[]
    find=[]
    allfind=[]
    
    
    x=0
    #A和B函数完成n列表中数字的组合
    def A():
        m.append(n[0])
        n.pop(0)
    
    def B():
        if len(n)>1:
            m.append(n[0]*10+n[1])
            for l in range(0,2):
                n.pop(0)
        else:
            A()
    #C和D函数完成被分配后数字的计算，并把计算的过程记录在v列表中        
    def C(x):
        
        x=x+m[0]
        m.pop(0)
        v.append('+')
        
    def D(x):
       
        x=x-m[0]
        m.pop(0)
        v.append('-')
        
     
    
    
    
        
    #引入随机变量，把以上的ABCD函数进行随机运算，实现不同的组合情况运算。
    import random
    
    while x!=y:
    
    
        while len(n)>0:
            z = random.randint(0,1)
        
            if z==0:
                A()
            elif z==1:
                B()
        f=m[:]
            
        while len(m)>0:
            if len(v)==0:
                z=0
            else:
                z = random.randint(0,1)
            
            if z==0:
                x=x+m[0]
                C(x)
            elif z==1:
                x=x-m[0]
                D(x)
        #当每次运算的结果x为目标结果y时，把计算过程中的数字组合和运算符号组合成算式
        if x==y:
                
                while len(v)>0:
                    
                    find.append(v[0])
                    v.pop(0)
                    find.append(f[0])
                    f.pop(0)
                 
                return(find)
               
        else:
            n=[1,2,3,4,5,6,7,8,9]
            v=[]
            x=0
            
          
#重复n次随机组合运算得到全部符合结果的情况
def Find_expression(y):            
    allfind=[]  
    n=1000         
    for i in range(0,n):
      a=expression(y)
      if a not in allfind:
          allfind.append(a)
          
      
    print(allfind)
    print('resuls='+str(len(allfind)))

#总函数
Find_expression(50)
    
      