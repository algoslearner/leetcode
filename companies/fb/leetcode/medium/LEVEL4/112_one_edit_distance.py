'''
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.
 

Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.
 

Constraints:

0 <= s.length, t.length <= 104
s and t consist of lowercase letters, uppercase letters, and digits.
'''

# two pointers, TC: O(max(n,m)), SC: O(1)
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        
        found_inequality = False
        i = j = 0
        
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if found_inequality: return False
                found_inequality = True
                
                if len(s) < len(t): 
                    i -= 1
                elif len(s) > len(t):
                    j -= 1
            i += 1
            j += 1
        return True
