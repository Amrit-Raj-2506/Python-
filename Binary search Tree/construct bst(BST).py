#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):
    
    if not 1st:
        return None
    mid=len(1st)//2
    root=BinaryTreeNode(1st[mid])
    root.left=constructBST([:mid])
    root.right=constructBST([mid+1:])
    return root
    # Given a sorted integer array A of size n which contains all unique
    # elements. You need to construct a balanced BST from this input array.
    # Return the root of constructed BST. If array size is even, take first mid
    # as root.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    pass

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
lst=[int(i) for i in input().strip().split()]
root=constructBST(lst)
preOrder(root)

