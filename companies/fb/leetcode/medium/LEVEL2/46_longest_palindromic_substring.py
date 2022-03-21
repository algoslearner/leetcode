'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

# Brute force
# TC: O(n^3)
# SC: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""
        maxlen = 0
        
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                cand = s[i:j]
                
                if cand == cand[::-1] and len(cand) > maxlen:
                    output = cand
                    maxlen = len(cand)
            
        return output
        

 # OPTIMIZED : expand from center     
