#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelWise(root):
    if queue is None:
        return
    q=queue.Queue()
    q.put(root)
    
    while not q.empty():
        firstnode=q.get()
        print (firstnode.data,end=':')
    	
        if firstnode.left != None:
        	q.put(firstnode.left)
        	print('L:',firstnode.left.data,end=',')
        if firstnode.left==None:
            print('L:',-1,end=',')
        if firstnode.right != None:
            q.put(firstnode.right)
            print('R:',firstnode.right.data,end='')
        if firstnode.right==None:
            print('R:',-1,end='')
        print()
        

    
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
printLevelWise(root)

