## Assignment 1- Factorial
Write a program that takes a number as input and prints its factorial as output.

**Input Format:**

Single line of input contains a number

**Output Format:**

Display the value of the factorial corresponding to the input

**Example:**

__Input:__

3

__Output:__

6

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
    
n = int(input())
print(fact(n),end = "")
```
