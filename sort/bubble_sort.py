# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:24:07 2020
https://www.cnblogs.com/onepixel/p/7674659.html
"""
# best time complexity for sort  sort
#bubble sort O(N^2) 稳定

def bubble_sort(x):
    for i in range(0, len(x)-1):
        for j in range(0, len(x)-1-i):   #O(n + n-1 +n-2 + ....1)= O(n^2)
            if x[j]>x[j+1]:
                temp = x[j]
                x[j] = x[j+1]
                x[j+1]=temp
    return x
                
x5=[1,5,8,2,3,9,7]
x1=[1]
x2=[]
x3=[-1 -5, -3, -8,-10,-4]
x4= [9,8,7,6,5,4,3,2]

for x in [x1, x2, x3, x4, x5]:
    x_unsort=x.copy()
    x_sort = bubble_sort(x)
    print(x_unsort)
    print(x_sort)
    print("-----------")
