#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele = ele
        self.priority = priority
       
class PriorityQueue:
    def __init__(self):
        self.pq = []
   
    def isEmpty(self):
        return self.getSize() == 0
   
    def getSize(self):
        return len(self.pq)

    def getMax(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele
   
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
           
            if self.pq[parentIndex].priority < self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
           
    def insert(self,ele,priority):
        pqNode = PriorityQueueNode(ele,priority)
        self.pq.append(pqNode)
        self.__percolateUp()
       
    def removeMax(self):
        if self.isEmpty():
            return  None
        temp=self.pq[0]
        self.pq[0]=self.pq[len(self.pq)-1]
        self.pq.pop()
        i=0
   
        while((2*i+1)<len(self.pq) or (2*i+2)<len(self.pq)):
            t1=self.pq[i].priority
            j=-1
            if 2*i+1>=len(self.pq) and self.pq[2*i+2].priority>t1:
              j=2*i+2
              self.pq[i],self.pq[j]=self.pq[j],self.pq[i]
            elif 2*i+2>=len(self.pq) and self.pq[2*i+1].priority>t1:
              j=2*i+1
              self.pq[i],self.pq[j]=self.pq[j],self.pq[i]
            elif 2*i+1>=len(self.pq):
                j=(-1)
            elif 2*i+2>=len(self.pq):
                j=(-1)
            elif self.pq[2*i+1].priority>t1 or self.pq[2*i+2].priority>t1:
                k=max(self.pq[2*i+1].priority,self.pq[2*i+2].priority)
                if k==self.pq[2*i+1].ele:
                    j=2*i+1
                else:
                    j=2*i+2
                self.pq[i],self.pq[j]=self.pq[j],self.pq[i]
            if j==-1:
                break
            i=j
        return temp.ele
               
               
               
        #Implment This Function Here
        pass
       
myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1

