# https://leetcode.com/problems/longest-palindrome/
'''
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''

#############################################################################################################
# TC: O(n)
# SC: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqmap = {}
        for c in s:
            freqmap[c] = freqmap.get(c, 0) + 1
        
        length = 0
        for freq in freqmap.values():
            length += freq // 2 * 2
            if length % 2 == 0 and freq % 2 == 1:
                length += 1
        return length
            
