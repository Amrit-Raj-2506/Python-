#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def append_LinkedList(head,n) :
    if head==None or n<0:
        return None
    result=0
    cur=head
    prev=head
    while(cur and n!= result):
        result+=1
        cur=cur.next
    if cur==None:
        return None
    next=cur.next
    while next:
        cur=next
        next=cur.next
        prev=prev.next
        
    cur.next=head
    cur=prev.next
    prev.next=None
    return cur

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
l = append_LinkedList(l, i)
printll(l)

