#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def sort(x,y,z):
    li=[x,y,z]
    max=x
    if max<=y:
        max=y
    if max<=z:
        max=z
    li.remove(max)
    if li[0]>=li[1]:
        print(li[1]," ",li[0]," ",max)
    else:
        print(li[0]," ",li[1]," ",max)
       
   
n=int(input())
lis=[int(x) for x in input().split()]
a=int(input())
for x in range(0,n,1):
    c=0
    for i in range(x+1,n,1):
        k=a-lis[x]-lis[i]
        if k in lis[i+1:]:
            c=lis[i+1:].count(k)
            for q in range(c):
                sort(lis[x],lis[i],k)

