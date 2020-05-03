#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def power(x, n):
    
    if n==0:
        return 1
    if x>= 0:
        ans=x**n
    return ans
    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))

