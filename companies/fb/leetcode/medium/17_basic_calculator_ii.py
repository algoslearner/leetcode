'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
'''

class Solution:
    def calculate(self, s: str) -> int:
        
        # USING STACK
        # Time : O(n)
        # Space : O(n)
        op, val = "+", 0 #initialized at "+0"
        stack = []
        for i, x in enumerate(s):
            if x.isdigit(): val = 10*val + int(x) #accumulating digits 
                
            if x in "+-*/" or i == len(s) - 1: #
                if   op == "+": stack.append(val)
                elif op == "-": stack.append(-val)
                elif op == "*": stack.append(stack.pop() * val)
                elif op == "/": stack.append(int(stack.pop()/val))
                op, val = x, 0 #reset 
        return sum(stack)
        
        # using loop
        # Time : O(n)
        # Space : O(1)
        '''
        inner, outer, result, opt = 0, 0, 0, '+'
        for c in s + '+':
            if c == ' ': continue
            if c.isdigit():
                inner = 10 * inner + int(c)
                continue
            if opt == '+':
                result += outer
                outer = inner
            elif opt == '-':
                result += outer
                outer = -inner
            elif opt == '*':
                outer = outer * inner
            elif opt == '/':
                outer = int(outer / inner)
            inner, opt = 0, c
        return result + outer
        '''
        
