# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 14:23:13 2020

"""


# insert sort O(N^2) 稳定
#example:
import numpy as np

x5=[1,5,8,2,3,9,7]
x1=[1]
x2=[]
x3=[-1 -5, -3, -8,-10,-4]
x4= [9,8,7,6,5,4,3,2]

#O(cN)=O(N) c is constant known
#O(N+a)=O(n)

def insert_sort(x):
    for i in range(1, len(x)):   #O(n)
        j = i - 1                #O(n)=O(n-1)    
        key = x[i]               #O(n)=O(n-1)    
        while j >= 0 and x [j] > key: # O(n^2)
            x[j+1] = x[j]        # O(n^2)       # if key is not stored, then this will change x[i] to x[i-1], then we cannot test x[j]>x[i]
            j = j - 1            # O(n^2)
                              
        x[j+1]= key;
    return x

# in total O(n)
#空间复杂度 自己新建了几个变量， 这里是1 个所以是 O(1)
for x in [x1, x2, x3, x4, x5]:
    x_unsort=x.copy()
    x_sort = insert_sort(x)
    print(x_unsort)
    print(x_sort)
    print("-----------")
    
# list dictionary set 可变 mutable  ， pass by reference  
# bool int float tuple str frozenset  不可变 , pass by value