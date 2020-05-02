#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def uniqueChars(string):
    words=list(string)
    d={}
    for w in words:
        if w in d:
            d[w]=d[w]+1
    	
        else:
            print (w,end='')
            d[w]=1
    	
    # Please add your code here
    pass

    # Please add your code here


# Main
string = input()
(uniqueChars(string))

