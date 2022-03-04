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

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def longestPalindrome(self, s: str) -> str:
        # so I want to create frames of different lengths
        # that will move along a string
        # so if string is abba
        # the first frame is abba
        # the second iteration be: abb, bba
        # third iteration be: ab, bb, ba
        # we start with widest frame, because we are after longest
        # palindromic substring
        # right off the bat check if the input itself is a non empty palindromic string
        if not s:
            raise Exception("You werent supposed to be null")
            
        if self.isPalindrome(s):
            return s
                
        for i in range(len(s), 0, -1):
            for j in range(0, len(s)-i+1): 
                candidate = s[j:j+i]
                if self.isPalindrome(candidate):
                    return candidate
                
# EXPAND FROM CENTER: METHOD 2: TC:O(n2)
def longestPalindrome(self, s):
    self.maxlen = 0
    self.start = 0
    
    for i in range(len(s)):
        self.expandFromCenter(s,i,i)
        self.expandFromCenter(s,i,i+1)
    return s[self.start:self.start+self.maxlen]
    

def expandFromCenter(self,s,l,r):
    while l > -1 and r < len(s) and s[l] ==s[r]:
        l -= 1
        r += 1
    
    if self.maxlen < r-l-1:
        self.maxlen = r-l-1
        self.start = l + 1
        
# OPTIMIZED
class Solution:
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
                

        
