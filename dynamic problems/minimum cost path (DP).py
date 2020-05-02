#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
def min_path(m,n,arr,i,j):
    if i==m-1 and j==n-1:
        return arr[i][j]
    if i>=m or j>=n:
        return sys.maxsize
    
    ans1 = min_path(m,n,arr,i+1,j)
    ans2 = min_path(m,n,arr,i,j+1)
    ans3 = min_path(m,n,arr,i+1,j+1)
    
    ans = arr[i][j] + min(ans3,ans2,ans1)
    
    return ans
arr=[]
m,n = input().split()
m = int(m)
n = int(n)

for x in range(m):
    arr.append([int(y) for y in input().split()])

    
print(min_path(m,n,arr,0,0))

