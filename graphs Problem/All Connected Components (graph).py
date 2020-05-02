#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue
class Graph:
    def __init__(self,n):
        self.n=n
        self.adj=[[0 for i in range(self.n)] for j in range(self.n)]
   
    def addEdges(self,v1,v2):
        self.adj[v1][v2]=1
        self.adj[v2][v1]=1
   
    def bfsUtil(self, u, visited):
        q=queue.Queue()
        q.put(u);l=[]
        visited[u]=True
        while not q.empty():
            u=q.get()
            l.append(u)
            for i in range(self.n):
                if self.adj[u][i]>0 and not visited[i]:
                    q.put(i)
                    visited[i]=True
        l.sort()
        for x in l:
            print(x,end=" ")
        print()
           
    def bfs(self):
        visited = [False for i in range(self.n)]
        for i in range(self.n):
            if visited[i] == False:
                self.bfsUtil(i, visited)

#     def __ccHelper(self, sv, visited, m):
       
#         m.append(sv)
#         visited[sv] = True
#         for i in range(self.nVerticies):
#             if self.adjMatrix[sv][i] > 0 and visited[i] is False:
#                 self.__ccHelper(i, visited, m)
               
#         return m
#     def connectedComponents(self):
#         visited = [False for i in range(self.nVerticies)]
#         for i in range(self.nVerticies):
#             if visited[i] is False:
#                 com = self.__ccHelper(i, visited, [])
#                 com.sort()
#                 for x in com:
#                     print(x,end=" ")
#                 print()
   
V,E=map(int,input().split())
g=Graph(V)
for i in range(E):
    v1,v2=map(int,input().split())
    g.addEdges(v1,v2)
g.bfs()

