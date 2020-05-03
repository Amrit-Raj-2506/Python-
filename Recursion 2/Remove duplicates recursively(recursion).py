#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    if len(string)==0 or len(string)==1:
        return string
    
    if string[0]==string[1]:
        return removeConsecutiveDuplicates(string[1:])
    else :
        return string[0]+removeConsecutiveDuplicates(string[1:])
    # Please add your code here
    pass

# Main
string = input().strip()

print(removeConsecutiveDuplicates(string))

