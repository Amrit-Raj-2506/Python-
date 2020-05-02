#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''def maxFreq(l):
    words=[int (i) for i in (l)]
    d={}
    for w in words:
        d[w]=d.get(w,0)+1
        
    max=0
    for w in d:
        freq=d[w]
        if freq>max:
            max=freq
            d=w
    		return d'''
def maxFreq(l): 
    d = {} 
    for num in l: 
        if num in d: 
            d[num] += 1 
        else: 
            d[num] = 1 
    ans = l[0] 
    for num in l: 
        if d[num] > d[ans]: 
            ans = num 
    return ans 


# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))

