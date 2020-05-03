#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def partition(arr,start, end):
    m=arr[start]
    c=0
    for i in range (start,end+1):
        if arr[i]<m:
            c=c+1
    arr[start+c],arr[start]=arr[start],arr[start+c]
    m1=start+c
         
    i=start
    j=end
    while i<j:
        if arr[i]<m:
            i=i+1
        elif arr[j]>=m:
            j=j-1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i=i+1
            j=j-1
    return m1


            
def sort (arr,start,end):
    if start>=end:
        return
    m1=partition(arr,start,end)
    sort(arr,start,m1-1)
    sort(arr,m1+1,end)
    

 # sorted arr 
# comparing arr3==arr(which is m1 now)
def intersection (arr,arr1):
    sort (arr,0,n-1)
    sort (arr1,0,n1-1)
    i=0
    j=0
    while i<len(arr) and j<len(arr1):
            if arr[i]<arr1[j]:
                i=i+1
            elif arr1[j]<arr[i]:
                j=j+1
            elif arr[i]==arr1[j]:
                print (arr1[j])
                i=i+1
                j=j+1
        
    # Please add your code here
    pass

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
intersection(arr,arr1)


