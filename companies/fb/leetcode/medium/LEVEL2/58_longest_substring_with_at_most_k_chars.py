'''
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
 

Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50
'''

# TC : O(n)

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start = 0
        freq = {}
        max_length = 0
        for end in range(len(s)):
            rightchar =s[end]
            if rightchar in freq:
                freq[rightchar] += 1
            else:
                freq[rightchar] = 1
            
            # check if sliding window has k distinct characters, then slide window by one character
            while len(freq) > k:
                leftchar = s[start]
                freq[leftchar] -= 1
                if freq[leftchar] == 0: 
                    del freq[leftchar]
                start += 1
            
            # recalculate max_length
            window_size = end - start + 1
            max_length = max(max_length, window_size)
        return max_length
