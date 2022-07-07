# https://leetcode.com/problems/minimum-window-substring/
'''
Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="aabdec", Pattern="abac"
Output: "aabdec"
Explanation: The smallest substring having all character occurrences of the pattern is "aabdec"
Example 3:

Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".
Example 4:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
'''

##################################################################################################################
# TC: O(N + M)
# SC: O(M)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # load pattern t to a hashmap
        freqmap = {}
        for c in t:
            freqmap[c] = freqmap.get(c, 0) + 1
        
        # parse the bigger string
        start = 0
        charmatch = 0
        
        min_length = len(s) + 1
        sub_start = 0
        for end in range(len(s)):
            right_char = s[end]
            if right_char in freqmap:
                freqmap[right_char] -= 1
                if freqmap[right_char] >= 0: charmatch += 1
            
            # check if pattern matched
            while charmatch == len(t):
                if min_length > end - start + 1:
                    min_length = end - start + 1
                    sub_start = start
                
                # slide window
                left_char = s[start]
                if left_char in freqmap:
                    if freqmap[left_char] == 0: charmatch -= 1
                    freqmap[left_char] += 1
                start += 1
             
        if min_length > len(s): return ""
        return s[sub_start : sub_start + min_length]
