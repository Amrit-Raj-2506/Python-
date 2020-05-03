#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def s(n):
    if n==0:
        return 0
    sum=n%10
    return sum+(s(int(n//10)))
n = int (input())
a = s(n)
print (a)

