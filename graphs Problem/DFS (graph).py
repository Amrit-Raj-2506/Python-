#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue
class built:
    def __init__(self,vertex):
        self.vertex=vertex
        self.matrix=[[0 for x in range(vertex)] for y in range(vertex)]
        self.visited=[False for x in range(vertex)]
    def addv(self,y):
        for i in range(y):
            l1=[int(x) for x in input().split() ]
            a,b=(l1[0],l1[1])
       
            self.matrix[a][b]=1
            self.matrix[b][a]=1
    def fp(self,p1,p2,path):
        # if self.matrix[p1][p2]==1:
        #     path.append(p2)
        #     return path,True
       
        if p1==p2:
            path.append(p1)
            return path,True
       
        self.visited[p1]=True
       
        for ele in range(self.vertex):
            if self.visited[ele]==False and self.matrix[p1][ele]==1:
               
                a,b=self.fp(ele,p2,path)
                if b==True:
                    #path.append(ele)
                    path.append(p1)
                    return path,True
        return path,False
           
       
       
       
l=[int(x) for x in input().split() ]
x=l[0]
y=l[1]
a=built(x)
a.addv(y)
la=[int(x) for x in input().split() ]
c=la[0]
b=la[1]
path=[]
k,t=a.fp(c,b,path)
if t:
    print(*k)

