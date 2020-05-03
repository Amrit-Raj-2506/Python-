#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def z(n):
    if n<=0:
        return 0
    if n%10==0:
        s= z(int(n//10))
        return s+1
    else:
        s=z(int(n//10))
        return s
n=int(input())
print(z(n))

