#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
#Write your code here
def isEmpty(stack):
    if len(stack)==0:
        return True
    else:
        return False
def getTop(stack):
    top=stack.pop()
    stack.append(top)
    return top
def countB(string):
    if len(string)== 0:
        return 0
    if len (string)%2 != 0:
        return -1
    stack=list()
    for i in range(len(string)):
        currentchar=string[i]
        if currentchar =='{':
            stack.append(currentchar)
        else:
            if not isEmpty(stack) and getTop(stack)=='{':
                stack.pop()
            else:
                stack.append(currentchar)
                
    count=0
    while not isEmpty(stack):
        char1=stack.pop()
        char2=stack.pop()
        if char1 !=char2:
            count+=2
        else:
            count+=1
            
	
    return count
string=input().strip()
print(countB(string))

