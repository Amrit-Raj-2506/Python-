#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Problem: Remove x from string
def removeX(string): 
    if len(string)==0:
        return string
    if string[0] != 'x':
        return string[0]+removeX(string[1:])
    else:
        return removeX(string[1:])
    
    pass

# Main
string = input()

print(removeX(string))

