#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def mu(m,n):
    if n==0 :
        return 0
    return m+mu(m,n-1)
import sys
sys.setrecursionlimit(10000)
n=int(input())
m=int(input())
a= mu(m,n)
print(a)

