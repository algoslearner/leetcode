# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/YQy7Lx79R0K
'''
Given a stair with ‘n’ steps, implement a method to count how many possible ways are there to reach the top of the staircase, 
given that, at every step you can either take 1 step, 2 steps, or 3 steps.

Example 1:

Number of stairs (n) : 3
Number of ways = 4
Explanation: Following are the four ways we can climb : {1,1,1}, {1,2}, {2,1}, {3} 
Example 2:

Number of stairs (n) : 4
Number of ways = 7
Explanation: Following are the seven ways we can climb : {1,1,1,1}, {1,1,2}, {1,2,1}, {2,1,1}, 
{2,2}, {1,3}, {3,1}
'''

###########################################################################################################################
# recursion
# TC: O(3^n) exponential with 3 recursive calls in one function
# SC : O(n)

def count_ways(n):
  if n == 0:
    return 1  # base case, we don't need to take any step, so there is only one way

  if n == 1:
    return 1  # we can take one step to reach the end, and that is the only way

  if n == 2:
    return 2  # we can take one step twice or jump two steps to reach at the top

  # if we take 1 step, we are left with 'n-1' steps;
  take1Step = count_ways(n - 1)
  # similarly, if we took 2 steps, we are left with 'n-2' steps;
  take2Step = count_ways(n - 2)
  # if we took 3 steps, we are left with 'n-3' steps;
  take3Step = count_ways(n - 3)

  return take1Step + take2Step + take3Step


def main():

  print(count_ways(3))
  print(count_ways(4))
  print(count_ways(5))


main()

###########################################################################################################################
# top down dp with memoization
# TC: O(n)
# SC: O(n)

def count_ways(n):
  memo = [-1 for _ in range(n + 1)]
  return count_ways_recursive(n, memo)


def count_ways_recursive(n, memo):
  if n == 0 or n == 1:
    return 1
  if n == 2:
    return 2

  if memo[n] > -1:
    return memo[n]
  
  memo[n] = count_ways_recursive(n - 1, memo) + count_ways_recursive(n - 2, memo) + count_ways_recursive(n - 3, memo)
  return memo[n]

###########################################################################################################################
# bottom up dp with tabulation
# TC: O(n)
# SC: O(n)

def count_ways(n):
  if n < 2:
    return 1
  if n == 2:
    return 2

  dp = [0 for x in range(n+1)]
  dp[0] = 1
  dp[1] = 1
  dp[2] = 2

  for i in range(3, n+1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

  return dp[n]

###########################################################################################################################
# bottom up dp + memory optimized
# TC: O(n)
# SC: O(1)

def count_ways(n):
  if n < 2:
    return 1
  if n == 2:
    return 2
  
  n1, n2, n3 = 1, 1, 2
  for i in range(3, n+1):
    n1, n2, n3 = n2, n3, n1+n2+n3
  return n3
