#!/usr/bin/env python
# coding: utf-8

# In[ ]:




def subsequences(string):
    if len(string)==0:
        output=[]
        output.append("")
        return output
    smallerstring=string[1:]
    smalleroutput=subsequences(smallerstring)
    
    output=[]
    for sub in smalleroutput:
        output.append(sub)
    for sub in smalleroutput:
        c=string[0]+sub
        output.append(c)
    return output
    
        
    #Implement Your Code Here
    pass


string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)





