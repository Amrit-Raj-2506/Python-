#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys,math,ceil

def minStepsTo1(n):
    if n == 0:
        return 0
    ans = sqrt(ceil(n))
    for i in range(1,n+1): 
        temp = i * i 
        if temp > n: 
            break
        else: 
            ans = min(ans, 1 + minStepsTo1(n - temp)) 
      
    return ans


        

    

n = int(input())
ans = minStepsTo1(n)
print(ans)

