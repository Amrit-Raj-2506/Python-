#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge(head1,head2):
    final_head=None
    final_tail=None
    if (head1.data<=head2.data):
        final_head=head1
        final_tail=head1
        head1=head1.next
    else:
        final_head=head2
        final_tail=head2
        head2=head2.next
    while head1 != None and head2 != None:
        if head1.data<=head2.data:
            final_tail.next=head1
            final_tail=final_tail.next
            head1=head1.next
        else:
            final_tail.next=head2
            final_tail=final_tail.next
            head2=head2.next
    while head1 is not None:
        final_tail.next=head1
        final_tail=final_tail.next
        head1=head1.next
    while head2 is not None:
        final_tail.next=head2
        final_tail=final_tail.next
        head2=head2.next
    final_tail.next=None
    return final_head
    

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
arr1=list(int(i) for i in input().strip().split(' '))
arr2=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l1 = ll(arr1[:-1])
l2 = ll(arr2[:-1])
l = merge(l1, l2)
printll(l)

