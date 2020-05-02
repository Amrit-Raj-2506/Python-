#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def knapsackBF(w, val, wt):
    n= len(val)
    dp=[[0 for j in range(w+1)]for i in range(n+1)]
    for i in range (1,n+1):
        for j in range (1,w+1):
            if j<wt[i-1]:
                ans=dp[i-1][j]
            else:
                ans1=val[i-1]+dp[i-1][j-wt[i-1]]
                ans2=dp[i-1][j]
                ans=max(ans1,ans2)
            dp[i][j]=ans
    return dp[n][w]
            
    #Implement Your Code Here
    pass

from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
w=list(int(i) for i in input().strip().split(' '))
val=list(int(i) for i in input().strip().split(' '))
wt=int(input())
print(knapsackBF(w, val, wt))

