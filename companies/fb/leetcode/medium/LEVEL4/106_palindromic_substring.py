'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
'''

# BRUTE FORCE: Check all substrings
# TC: O(N^3)
# SC: O(1)

class Solution:
    def isPalindrome(self, s: str, lo: int, hi: int) -> bool:
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True
    
    def countSubstrings(self, s: str) -> int:
        count = 0
        for lo in range(len(s)):
            for hi in range(lo,len(s)):
                count += self.isPalindrome(s,lo,hi)
        return count
      

############################################################################
# For optimizations READ: 
# https://leetcode.com/problems/palindromic-substrings/solution/
