#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def m(str):
    if len(str)==0 or len(str)==1:
        return str
    if str[0]==str[1]:
        e=m(str[1:])
        return str[0]+'*'+e
    else:
        e=m(str[1:])
        return str[0]+e
    
str=input().strip()
print (m(str))

    
        

