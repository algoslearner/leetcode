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

'''
the balance tells you what "depth" you are at since with each '(' we are increasing the depth by 1 (kind of similar to the concept in Solution 2).
the "cores" () are the only structure that provides value, the outer parentheses just add some multiplier to the cores. So we only need to be concerned with those.
With those 2 ideas in mind, we are able to calculate how much the "core" is worth directly without having to calculate substructures recursively and then apply multipliers.

E.g. For the example of ( ( ) ( ( ) ) ), 
with the stack method, we are calculating the inner structure ( ) ( ( ) ) first 
and then multiplying the score by 2. 

With the 3rd method, by knowing the depth of the core, 
we are actually performing this calculation ( ( ) ) + ( ( ( ) ) ).
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
