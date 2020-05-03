#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def si(str,n):
    if len(str)==1:
        return int(str)+(n*10)
    n=int(str[0:1])+(n*10)
    return si(str[1:],n)
str=input().strip()
print(si(str,0))

