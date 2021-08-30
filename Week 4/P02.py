# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 07:53:11 2021

@author: GEC DAHOD
"""
#Given a list of n integers, count the number of integers in the list that are 
#either a multiple of 3 or a multiple of 5. (All the numbers are guaranteed to be distinct).

a = list(map(int,input().split()))
ans = 0
for i in a:
  if(i%3==0):
    ans+=1
  elif (i%5==0):
    ans+=1
  else:
    pass
print(ans,end="")
