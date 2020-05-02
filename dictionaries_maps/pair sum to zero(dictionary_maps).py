#!/usr/bin/env python
# coding: utf-8

# In[ ]:




def pairSum0(l):
    d = {}
    for n in l:
        d[n] = d.get(n,0) + 1
    i = 0    
    for n in d:
        i = 0
        k = 1
        while i < len(l):
            if (l[i] + n) == 0:
                c1 = max(l[i],n)
                c2 = min(l[i],n)
                for k in range(d.get(n)):
                    print(c2,c1)
                d[l[i]] = 0        
            i = i + 1




n=int(input())
l=list(int(i) for i in input().strip().split(' '))
pairSum0(l)

