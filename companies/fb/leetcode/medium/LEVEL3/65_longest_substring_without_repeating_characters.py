'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

# TC: O(n)
# SC: O(n), hashmap

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcbacbb
        # start
        
        start = 0
        maxlen = 0
        hashmap = {}
        
        for i,c in enumerate(s):
            if c in hashmap and start <= hashmap[c]:
                # repeating char, then slide "start" by 1
                start = hashmap[c] + 1
            else:
                maxlen = max(maxlen, i-start+1)
            hashmap[c] = i
            
        return maxlen
        
