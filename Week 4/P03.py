# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 07:53:54 2021

@author: GEC DAHOD
"""
#Given a list of binary numbers (0s and 1s), determine the number of possible 
#arrangements of distinct binary sequences using given 0s and 1s.
def fact(n):
  if (n==1):
    return 1
  else:
    ans=1
    for i in range(1,n+1):
      ans = i*ans
    return ans

a = input().replace(" ", "")
c1 = 0
c2 = 0
for i in range(len(a)):
  if a[i] == '1':
    c1 += 1
  elif a[i] == '0':
    c2 += 1
  else:
    pass
ans = fact(len(a))//(fact(c1)*fact(c2))
print(ans,end="")