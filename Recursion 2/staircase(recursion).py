#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def r(n):
    if n<3:
        return n
    elif n==3:
        return 4
    return r(n-3)+r(n-2)+r(n-1)

n=int(input())
print (r(n))

