#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import queue


  
def reverse(q,k):
    if(k<=0 or  q.qsize() <=1):
        return
    ele=q.get()
    reverse(q,k-1)
    q.put(ele)
    return
def reverseFirstK(q,k):
    reverse(q,k)
    for i in range(q.qsize()-k):
        q.put(q.get())
#Implement Your Code Here     

        
from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
li = [int(ele) for ele in input().split()]
q = queue.Queue()
for ele in li:
	q.put(ele)
k = int(input())
reverseFirstK(q,k) 
while(q.qsize()>0):
	print(q.get())
	n-=1

