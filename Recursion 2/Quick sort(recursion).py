#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def partition(arr,arr1,start, end):
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

    m0=arr[start]
    c=0
    for i in range (start,end+1):
        if arr[i]<m:
            c=c+1
    arr[start+c],arr[start]=arr[start],arr[start+c]
    m2=start+c
         
    i=start
    j=end
    while i<j:
        if arr[i]<m0:
            i=i+1
        elif arr[j]>=m0:
            j=j-1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i=i+1
            j=j-1
    return m2
            
def sort (arr,arr1,start,end):
    if start>=end:
        return
    m1=partition(arr,arr1,start,end)
    sort(arr,arr1,start,m1-1)
    sort(arr,arr1,m1+1,end)
    
    m2=partition(arr,arr1,start,end)
    sort(arr,arr1,start,m2-1)
    sort(arr,arr1,m2+1,end)
  
 # sorted arr 
# comparing arr3==arr(which is m1 now)

    arr3=[]
    for i in range (0,len(arr)):
        for j in range(0,len(arr1)):
            if arr[i]<arr1[j]:
                i=i+1
            elif arr1[j]<arr[i]:
                j=j+1
            else:
                arr3.append(arr[i])
    return arr3
            
        
    # Please add your code here
    pass

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
a=sort(arr,arr1,0,n-1)
print(a)

