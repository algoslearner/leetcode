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

########################################################################################################################
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
        

 #########################################################################################################################
 # OPTIMIZED : expand from center     
 # TC: O(n^2)
 # SC: O(1)
 
 class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def palindromeIndex(l, r):
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                r += 1
                l -= 1
            return l+1,r
        
        start, end = 0, 0
        maxlen = 0
        for i in range(len(s)):
            # even palindrome
            l, r = palindromeIndex(i,i)
            if r -l > maxlen:
                maxlen = r - l
                start = l
                end = r
                
            # odd palindrome
            l, r = palindromeIndex(i, i+1)
            if r - l > maxlen:
                maxlen = r- l
                start = l
                end = r
        
        return s[start:end]
            

###########################################################################################################################
# another cleaner logic
# TC: O(n^2)
# SC: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):        
            odd  = self.palindromeAt(s, i, i)
            even = self.palindromeAt(s, i, i+1)
        
            res = max(res, odd, even, key=len)
        return res
 
    # starting at l,r expand outwards to find the biggest palindrome
    def palindromeAt(self, s, l, r):    
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
