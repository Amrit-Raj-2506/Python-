#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def u(arr):
    if len(arr)==0:
        return 0
    output = arr[0]
    for i in range(1,len(arr)):
        output=output^arr[i]
    return output
        
        
        
        
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
a=u(arr)
print(a)

