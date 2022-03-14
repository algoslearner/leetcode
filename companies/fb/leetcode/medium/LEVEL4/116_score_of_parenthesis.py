'''
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
 

Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
'''

# STACK
# TC: O(N)
# SC: O(N)

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0] #The score of the current frame

        for x in s:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()

# COUNT CORES, TC: O(N), SC: O(1)
'''
Intuition
The final sum will be a sum of powers of 2, as every core (a substring (), with score 1) 
will have it's score multiplied by 2 for each exterior set of parentheses that contains that core.

Algorithm

Keep track of the balance of the string, as defined in Approach #1.
For every ) that immediately follows a (, the answer is 1 << balance, 
as balance is the number of exterior set of parentheses that contains this core.
'''

class Solution(object):
    def scoreOfParentheses(self, S):
        ans = bal = 0
        for i, x in enumerate(S):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if S[i-1] == '(':
                    ans += 1 << bal
        return ans
