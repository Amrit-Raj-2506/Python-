#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Rotate(arr, d):
    n=len(arr)
    for i in range (0,d):
        t=arr[0]
        for i in range (n-1):
            arr[i]=arr[i+1]
        arr[n-1]=t
	    # Please add your code here
    pass

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
d=int(input())
Rotate(arr, d)
print(*arr)

