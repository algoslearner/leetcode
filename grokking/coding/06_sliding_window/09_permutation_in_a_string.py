# https://leetcode.com/problems/permutation-in-string/
'''
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters, it will have n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
'''

#################################################################################################################
# sliding window
# TC: O(N)
# SC: O(1)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # store pattern string s1 in hashmap
        freqmap = {}
        for c in s1:
            freqmap[c] = freqmap.get(c, 0) + 1
        
        # check in s2
        start = 0
        charmatch = 0
        for end in range(len(s2)):
            right_char = s2[end]
            if right_char in freqmap:
                freqmap[right_char] -= 1
                if freqmap[right_char] == 0: charmatch += 1
            
            # found permutation
            if charmatch == len(freqmap):
                return True
            
            # slide window: window size same as pattern
            if end >= len(s1) - 1:
                left_char = s2[start]
                if left_char in freqmap:
                    if freqmap[left_char] == 0: charmatch -= 1
                    freqmap[left_char] += 1
                start += 1
            
        return False
        
        
