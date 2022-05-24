# https://leetcode.com/problems/longest-valid-parentheses/
'''
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
'''

################################################################################################
# STACK
# TC: O(N)
# SC: O(N)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        stack = [-1]
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    maxans = max(maxans, i - stack[-1])
                else:
                    stack.append(i)
        return maxans
      
################################################################################################
# Two pointers : No extra space
# TC: O(N)
# SC: O(1)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        
        open_ = close = 0
        ans1 = 0
        for i in s:
            if i =='(':
                open_ += 1
            else:
                close += 1
            if open_ == close:
                ans1 = max (ans1, 2 * close)
            elif close > open_:
                open_ = close = 0
                
        ans2 = 0
        open_ = close = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                open_ += 1
            else:
                close += 1
            if open_ == close:
                ans2 = max(ans2,2*open_)
            elif open_ > close:
                open_ = close = 0
        
        maxans = max(ans1,ans2)
        return maxans
                
                
