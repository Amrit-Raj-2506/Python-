#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Problem ID 331 even after odd in a LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arrange_LinkedList(head):
    oddhead=None
    oddtail=None
    evenhead=None
    eventail=None
    while head is not None:
        if head.data%2==0:
            if evenhead is None:
                evenhead=head
                eventail=head
            else:
                eventail.next=head
                eventail=head
        else:
            if oddhead is None:
                oddhead=head
                oddtail=head
            else:
                oddtail.next=head
                oddtail=head
        head=head.next 
        
    if oddhead is None:
        return evenhead
    elif eventail is None:
        return oddhead
    else:
        oddtail.next=evenhead
        eventail.next=None
        return oddhead

    
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
l = arrange_LinkedList(l)
printll(l)

