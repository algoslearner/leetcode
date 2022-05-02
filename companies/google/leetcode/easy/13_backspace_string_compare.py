# https://leetcode.com/problems/backspace-string-compare/
'''
844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?
'''

################################################################################################
# Using stack
# TC: O(n)
# SC: O(n)

class Solution:
    def check(self, s: str) -> str:
        stack = []
        for c in s:
            if c != '#':
                stack.append(c)
            elif stack and c == '#':
                stack.pop()
        return "".join(stack)
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.check(s) == self.check(t)
      
################################################################################################
# Using two pointers
# TC: O(n)
# SC: O(1)
# https://leetcode.com/problems/backspace-string-compare/discuss/145786/Python-tm

class Solution(object):
    def backspaceCompare(self, S1, S2):
        r1 = len(S1) - 1 
        r2 = len (S2) - 1
        
        while r1 >= 0 or r2 >= 0:
            char1 = char2 = ""
            if r1 >= 0:
                char1, r1 = self.getChar(S1, r1)
            if r2 >= 0:
                char2, r2 = self.getChar(S2, r2)
            if char1 != char2:
                return False
        return True
        
    
    def getChar(self, s , r):
        char, count = '', 0
        while r >= 0 and not char:
            if s[r] == '#':
                count += 1
            elif count == 0:
                char = s[r]
            else:
                count -= 1
            r -= 1
        return char, r
