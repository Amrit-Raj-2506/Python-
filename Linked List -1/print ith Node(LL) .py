#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
def ithNode(head, i): 
    curr = head 
          
    l = 0
    while curr.next is not None: 
        curr = curr.next
        l += 1
         
    if i > l: 
        return
    curr = head 
    for j in range(0,  i): 
        curr = curr.next
    
    return curr
    pass

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
node = ithNode(l, i)
if node:
    print(node.data)

