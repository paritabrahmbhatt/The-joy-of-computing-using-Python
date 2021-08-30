## Assignment 2 - Multiples

Given a list of n integers, count the number of integers in the list that are either a multiple of 3 or a multiple of 5. (All the numbers are guaranteed to be distinct).

**Input Format:**

Single line of input contains a list of space separated integers 

**Output Format:**

Print the count of numbers that are divisible either by 3 or 5

**Example:**

**Input:**

1 3 5 6 7 9 11 13 15 18 20 21

**Output:**

8
__*Solution*__
```
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
```
