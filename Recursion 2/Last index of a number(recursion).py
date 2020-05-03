#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def firstIndex(arr, x,si):
    l=len(arr)
    if si==0:
        return -1
    elif arr[si]==x:
        return si
    
    return firstIndex(arr, x,si-1)
        
     
    
    # Please add your code here
    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x,n-1))

