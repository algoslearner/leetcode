# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/gx6jmzrMwgZ
'''
Write a function to calculate the nth Fibonacci number.

Fibonacci numbers are a series of numbers in which each number is the sum of the two preceding numbers. First few Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, …
'''

################################################################################################################################
# Recursion
# TC: O(2^n) is exponential
# SC: O(n) due to recursion stack

def calculateFibonacci(n):
  if n < 2:
    return n
  return calculateFibonacci(n - 1) + calculateFibonacci(n - 2)


def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()

'''
Output: 0.8s
5th Fibonacci is ---> 5
6th Fibonacci is ---> 8
7th Fibonacci is ---> 13
'''


################################################################################################################################
# Top down dp + memoization
# TC: O(n)
# SC: O(n) 

def calculateFibonacci(n):
  memo = [-1 for _ in range(n+1)]
  return calculateFibonacci_recursive(n, memo)

def calculateFibonacci_recursive(n, memo):
  if n < 2:
    return n
  
  if memo[n] >= 0:
    return memo[n]
  
  memo[n] = calculateFibonacci_recursive(n - 1, memo) + calculateFibonacci_recursive(n - 2, memo)
  return memo[n]

################################################################################################################################
# bottom up dp with tabulation
# TC: O(n)
# SC: O(n) 

def calculateFibonacci(n):
  if n < 2:
    return n
  dp = [0, 1]
  for i in range(2, n + 1):
    dp.append(dp[i - 1] + dp[i - 2])

  return dp[n]

################################################################################################################################
# bottom up dp with tabulation + optimized memory
# TC: O(n)
# SC: O(1) 

def calculateFibonacci(n):
  if n < 2:
    return n

  n1, n2, temp = 0, 1, 0
  for i in range(2, n + 1):
    temp = n1 + n2
    n1 = n2
    n2 = temp

  return n2
