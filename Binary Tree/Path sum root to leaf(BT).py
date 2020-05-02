#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rootToLeafPathsSumToK(root,sum,k,st):
    
    if root == None : 
        return

    k += root.data 
      
     
    st.append(root.data)  
  
 
    if (k == sum ) : 
      
        print('')  
        for i in range(len(st)): 
            print(st[i], end = " ")  
  
        print()  
      
      
    if (root.left != None) : 
        rootToLeafPathsSumToK(root.left, sum,k, st)  
  
      
    if (root.right != None) : 
        rootToLeafPathsSumToK(root.right, sum,k, st) 
    

  
      
    st.pop(-1)  
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    pass

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
sum=int(input())
rootToLeafPathsSumToK(root,sum, 0, [])

