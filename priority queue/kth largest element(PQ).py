#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
def kthLargest(lst, k):
    heap=lst[:k]
    heapq.heapify(heap)
    n=len(lst)
    for i in range(k,n):
        if heap[0]<lst[i]:
            heapq.heapreplace(heap,lst[i])
    return heap
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    pass

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans[0])

