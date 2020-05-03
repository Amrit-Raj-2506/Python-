#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def getstring(d):
    if d==2:
        return "abc"
    if d==3:
        return"def"
    if d==4:
        return"ghi"
    if d==5 :
        return "jkl"
    if d==6:
        return "mno"
    if d==7 :
        return "pqrs"
    if d==8:
        return "tuv"
    if d==9:
        return "wxyz"
    
    return " "
def keypad(n):
    if n==0:
        output=[]
        output.append("")
        return output
    smallernumber=n//10
    lastdigit=n%10
    
    smalleroutput=keypad(smallernumber)
    optionforlastdigit=getstring(lastdigit)
    output=[]
    for s in smalleroutput:
        for c in optionforlastdigit:
            option=s+c
            output.append(option)
    return output
        
    
    #Implement Your Code Here
    pass

n = int(input())
ans = keypad(n)
for s in ans:
    print(s)

