#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
def checkMaxHeap(lst):
    n=len(lst)
    
    for i in range (n):
        parentIndex=i
        rightChild=2*i+2
        leftChild=2*i+1
        if leftChild<n and lst[leftChild]>lst[i]:
            return False
        if rightChild<n and lst[rightChild]>lst[i]:
            return False
        
    return True
        
        
        
        
    
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    pass

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')

