#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def z(n):
    if n==0:
        return 1.00000
    return (1/2)**(n)+z(n-1)
n=int(input())
a= z(n)
print("%0.5f"%a)

