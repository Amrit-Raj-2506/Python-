#!/usr/bin/env python
# coding: utf-8

# In[ ]:




def checkBalanced(expr):
    sum= 0
    sum1= 0
    for i in range(len(expr)): 
        if (expr[i] == '(' and expr[i + 1] == ')'): 
            return True 
        if (expr[i] == '*' or expr[i] == '+' or expr[i] == '-' or expr[i] == '/'): 
            sum += 1 
        if (expr[i] == '('): 
            sum1 += 1 
      
    if (sum1 > sum): 
        return True 
    return False 

        
    

expr= input()
ans = checkBalanced(expr)
if ans is True:
    print('true')
else:
    print('false')




