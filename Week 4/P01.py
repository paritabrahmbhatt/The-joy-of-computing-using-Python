# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 07:52:10 2021

@author: GEC DAHOD
"""
#Write a program that takes a number as input and prints its factorial as output.
def fact(n):
  if (n==1):
    return 1
  else:
    ans=1
    for i in range(1,n+1):
      ans = i*ans
    return ans
    
n = int(input())
print(fact(n),end = "")