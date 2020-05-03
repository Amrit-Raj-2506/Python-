#!/usr/bin/env python
# coding: utf-8

# In[ ]:




def stockSpan(price,n):
    s= [None]*n
    s[0]=1
    for i in range (1,n,):
        s[i]=1
        j=i-1
        while j>=0 and price[i]>price[j]:
            s[i]+=1
            j-=1
    return s

        
    
        

#### Implement Your Code Here

n = int(input())
price = [int(ele) for ele in input().split()]
spans = stockSpan(price,n)
for ele in spans:
    print(ele,end= ' ')






