#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# code is not complete as for the last case the recursion limit exceeds in python .
#include <bits/stdc++.h>
using namespace std;

int buyTicket (int *arr, int n, int k){
deque <int> dq;
    priority_queue<int> pq;
   
    int yourPriority=arr[k];
    int time=1;
    for(int i=0;i<n;i++){
        if(i==k)
            dq.push_back(-1);
        else
            dq.push_back(arr[i]);
        pq.push(arr[i]);
    }
    //cout<<yourPriority<<" "<<pq.top()<<endl;
    if(yourPriority==pq.top()){
        for(int i=0;i<n;i++){
            if(dq[i]==pq.top())
                time++;
            else if(dq[i]==-1)
                return time;
        }
    }

    while(pq.top()>yourPriority || dq.front()!=-1){
       
       
        if(yourPriority==pq.top()){
        for(int i=0;i<dq.size();i++){
            if(dq[i]==pq.top())
                time++;
            else if(dq[i]==-1)
                return time;
            }
        }
       
        while(dq.front()!=pq.top()){
            dq.push_back(dq.front());
            dq.pop_front();
        }
        time++;
        dq.pop_front();
        pq.pop();
    }
    return time;
}

