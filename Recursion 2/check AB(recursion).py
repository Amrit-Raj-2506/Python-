#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def t(str):
    if len(str)==0 :
        return True
    if str[0]== 'a' and len(str)>=1:
        if str[1:3]=='bb':
            return t(str[3:])
        else:
            return t(str[1:])
        
        
    else :
        return False
    


str=input()
if t(str):
    print ('true')
else:
    print('false')
    
    

