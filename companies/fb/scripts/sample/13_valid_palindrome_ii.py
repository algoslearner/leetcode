'''
Valid palindrome
https://leetcode.com/problems/valid-palindrome-ii/ - Solved this in optimal way, explained time and space complexity.
'''

'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
'''

class Solution: 
    def validPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one = s[left:right]
                two = s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            
            left = left + 1
            right = right - 1
        return True
    
