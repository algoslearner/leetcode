# 
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

############################################################################################################################
# TC: O(N^2)
# SC: O(1)

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s+s
      
      
############################################################################################################################
# KMP
# TC: O(N)
# SC: O(N)
# https://leetcode.com/problems/rotate-string/discuss/765553/Python-O(N)-Solution-KMP-(made-easy)-beats-99

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if len(A) == 0: return True
        
        # capture length of strings
        # then make both strings 1 indexed
        N = len(A)
        A = " " + A + A
        B = " " + B
        
        # calculate pi table, it captures the length of the
		    # longest prefix that is also the suffix
        pi = [0] * (N+1)
        left, pi[0] = -1, -1
        for right in range(1, N+1):
            while left >= 0 and B[left + 1] != B[right]:
                left = pi[left]
            left += 1
            pi[right] = left
        
        # do matching
        j = 0
        for i in range(1, (2*N)+1):
            while j >= 0 and B[j+1] != A[i]:
                j = pi[j]
            j += 1
            if j == N: return True
        
        return False
