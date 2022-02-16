'''
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

 

Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
 

Constraints:

1 <= s.length <= 1000
s[i] is either '(' or ')'.
'''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        if s.isspace():
            return 0
        
        # TC : O(N)
        # SC : O(N)
        '''
        stack = []
        stack2 = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack: 
                    stack.pop()
                else:
                    stack2.append(c)
                    
        
        return len(stack2) + len(stack)
        '''
        
        # TC : O(N)
        # SC : O(1)
        opening = 0
        closing = 0
        
        for c in s:
            if c == '(':
                opening += 1
            else:
                if opening:
                    opening -= 1
                else:
                    closing += 1
        return opening + closing
            
            
        
