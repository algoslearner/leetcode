# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/NE52PnMY376
'''
Given a number ‘n’, implement a method to count how many possible ways there are to express ‘n’ as the sum of 1, 3, or 4.

Example 1:

n : 4
Number of ways = 4
Explanation: Following are the four ways we can express 'n' : {1,1,1,1}, {1,3}, {3,1}, {4} 
Example 2:

n : 5
Number of ways = 6
Explanation: Following are the six ways we can express 'n' : {1,1,1,1,1}, {1,1,3}, {1,3,1}, {3,1,1}, 
{1,4}, {4,1}
'''

########################################################################################################################
# recursion
# TC: O(3^n) exponentai;
# SC: O(n)

def count_ways(n):
  if n == 0:
    return 1  # base case, we don't need to subtract any thing, so there is only one way

  if n == 1:
    return 1  # we take subtract 1 to be left with zero, and that is the only way

  if n == 2:
    return 1  # we can subtract 1 twice to get zero and that is the only way

  if n == 3:
    return 2  # '3' can be expressed as {1, 1, 1}, {3}

  # if we subtract 1, we are left with 'n-1'
  subtract1 = count_ways(n - 1)
  # if we subtract 3, we are left with 'n-3'
  subtract3 = count_ways(n - 3)
  # if we subtract 4, we are left with 'n-4'
  subtract4 = count_ways(n - 4)

  return subtract1 + subtract3 + subtract4


def main():

  print(count_ways(4))
  print(count_ways(5))
  print(count_ways(6))


main()

########################################################################################################################
# top down dp + memoization
# TC: O(n)
# SC: O(n)

def count_ways(n):
  memo = [-1 for _ in range(n+1)]
  return count_ways_recursive(n, memo)

def count_ways_recursive(n, memo):
  if n <= 2:
    return 1

  if n == 3:
    return 2 # {1, 1, 1}, {3}
  
  if memo[n] > -1:
    return memo[n]
  
  memo[n] = count_ways_recursive(n - 1, memo) + count_ways_recursive(n - 3, memo) + count_ways_recursive(n - 4, memo)
  return memo[n]

def main():
  print(count_ways(4))
  print(count_ways(5))
  print(count_ways(6))

main()


########################################################################################################################
# bottom up dp with tabulation
# TC: O(n)
# SC: O(n)

def count_ways(n):
  if n <= 2:
    return 1
  if n == 3:
    return 2
  
  dp = [0 for x in range(n+1)]
  dp[0] = 1
  dp[1] = 1
  dp[2] = 1
  dp[3] = 2

  for i in range(4, n+1):
    dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4]

  return dp[n]
