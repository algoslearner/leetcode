# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/7nAKN0Qz67r
'''
Given an array of positive numbers, where each element represents the max number of jumps that can be made forward from that element, write a program to find the minimum number of jumps needed to reach the end of the array (starting from the first element). If an element is 0, then we cannot move through that element.

Example 1:

Input = {2,1,1,1,4}
Output = 3
Explanation: Starting from index '0', we can reach the last index through: 0->2->3->4
Example 2:

Input = {1,1,3,6,9,3,0,1,3}
Output = 4
Explanation: Starting from index '0', we can reach the last index through: 0->1->2->3->8
'''

##################################################################################################################
# recursion
# TC: O(2^n)
# SC: O(n)

import math


def count_min_jumps(jumps):
  return count_min_jumps_recursive(jumps, 0)


def count_min_jumps_recursive(jumps, currentIndex):
  n = len(jumps)
  # if we have reached the last index, we don't need any more jumps
  if currentIndex == n - 1:
    return 0

  if jumps[currentIndex] == 0:
    return math.inf

  totalJumps = math.inf
  start, end = currentIndex + 1, currentIndex + jumps[currentIndex]
  while start < n and start <= end:
    # jump one step and recurse for the remaining array
    minJumps = count_min_jumps_recursive(jumps, start)
    start += 1
    if minJumps != math.inf:
      totalJumps = min(totalJumps, minJumps + 1)

  return totalJumps


def main():
  print(count_min_jumps([2, 1, 1, 1, 4]))
  print(count_min_jumps([1, 1, 3, 6, 9, 3, 0, 1, 3]))

main()

##################################################################################################################
# top down dp
# TC: O(n^2)
# SC: O(n)

import math


def count_min_jumps(jumps):
  dp = [0 for x in range(len(jumps))]
  return count_min_jumps_recursive(dp, jumps, 0)


def count_min_jumps_recursive(dp, jumps, currentIndex):
  n = len(jumps)
  # if we have reached the last index, we don't need any more jumps
  if currentIndex == n - 1:
    return 0

  if jumps[currentIndex] == 0:
    return math.inf

  # if we have already solved this problem, return the result
  if dp[currentIndex] != 0:
    return dp[currentIndex]

  totalJumps = math.inf
  start, end = currentIndex + 1, currentIndex + jumps[currentIndex]
  while start < n and start <= end:
    # jump one step and recurse for the remaining array
    minJumps = count_min_jumps_recursive(dp, jumps, start)
    start += 1
    if minJumps != math.inf:
      totalJumps = min(totalJumps, minJumps + 1)

  dp[currentIndex] = totalJumps
  return dp[currentIndex]


def main():

  print(count_min_jumps([2, 1, 1, 1, 4]))
  print(count_min_jumps([1, 1, 3, 6, 9, 3, 0, 1, 3]))


main()

##################################################################################################################
# botttom up dp with tabulation
# TC: O(n^2)
# SC: O(n)

import math

def count_min_jumps(jumps):
  n = len(jumps)
  # initialize with infinity, except the first index which should be zero as we
  # start from there
  dp = [math.inf for _ in range(n)]
  dp[0] = 0

  for start in range(n - 1):
    end = start + 1
    while end <= start + jumps[start] and end < n:
      dp[end] = min(dp[end], dp[start] + 1)
      end += 1

  return dp[n - 1]


def main():
  print(count_min_jumps([2, 1, 1, 1, 4]))
  print(count_min_jumps([1, 1, 3, 6, 9, 3, 0, 1, 3]))


main()
