#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def checkBalanced(expr):
    s=[]
    for char in expr:
        if char in '({[':
            s.append(char)
        elif char is')':
            if (not s or s [-1]!='('):
                return False
            s.pop()
        elif char is'}':
            if (not s or s [-1]!='{'):
                return False
            s.pop()
        elif char is']':
            if (not s or s [-1]!='['):
                return False
            s.pop()
    if not s :
        return True
    return False
expr=input()
ans=checkBalanced(expr)
if ans  :
    print("true")
else:
    print("false")
    

