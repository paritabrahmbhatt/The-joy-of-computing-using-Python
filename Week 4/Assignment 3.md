## Assignment 3
Given a list of binary numbers (0s and 1s), determine the number of possible arrangements of distinct binary sequences using given 0s and 1s.

**Input Format:**

Single line of input containing 0s and 1s

**Output Format:**

Print an integer value indicating the number of possible arrangements using given 0s and 1s

Example:

**Input:**

0 1 0 1

**Output:**

6

Explanation:

For the given input, the possible distinct binary sequences that can be formed are : 0011, 0101, 0110, 1001, 1010, 1100.

Hence the output is 6.

__*Solution*__
```
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
```
