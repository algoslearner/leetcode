'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''

#############################################################################
# BRUTE FORCE
# Intuition: We can generate all 2^{2n} sequences of '(' and ')' characters. Then, we will check if each one is valid.
# TC: O(2^2n * n)
# SC: O(2^2n * n)

class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans
      
#################################################################################
# BACKTRACKING
# Intuition and Algorithm
# Instead of adding '(' or ')' every time as in Approach 1, let's only add them when we know it will remain a valid sequence. 
# We can do this by keeping track of the number of opening and closing brackets we have placed so far.
# We can start an opening bracket if we still have one (of n) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans
