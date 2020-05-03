#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def equilibriumIndex(arr):
    ls=0
    sum1=0
    i=0
    while i<len(arr):
        sum1+=arr[i]
        i=i+1
    index=0
    while index<len(arr):
        rs=sum1-ls-arr[index]
        if ls==rs:
            return index
        ls=ls+arr[index]
        index+=1
    return -1
            

    
    # Please add your code here
    pass

# Main
n = int(input())
arr = [int(i) for i in input().strip().split()]
print(equilibriumIndex(arr))

