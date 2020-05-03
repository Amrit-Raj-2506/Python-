#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def p(s,o):
    if len(s)==0:
        print(o)
        return
    p(s[1:],o)
    
    nw=o+s[0]
    p(s[1:],nw)

s=input()
p(s,"")

