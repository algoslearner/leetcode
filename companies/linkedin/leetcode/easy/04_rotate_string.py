# https://leetcode.com/problems/rotate-string/
'''
796. Rotate String

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 

Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.
'''

##########################################################################################################
# BRUTE FORCE
# TC: O(N^2)
# SC: O(1)

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if len(s) == 0:
            return True

        for j in range(len(s)):
            if all(s[(j + i) % len(s)] == goal[i] for i in range(len(s))):
                return True
        return False
      
##########################################################################################################
# SIMPLE CHECK
# TC: O(N^2)
# SC: O(N)

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s+s

