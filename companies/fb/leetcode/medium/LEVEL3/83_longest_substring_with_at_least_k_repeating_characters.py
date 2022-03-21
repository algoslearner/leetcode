'''
Given a string s and an integer k, 
return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

 

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
'''

######################################################################################################################
# check for character which does not satisy the condition
'''
# https://ttzztt.gitbooks.io/lc/content/string/longest-substring-with-at-least-k-repeating-characters.html
Thoughts:

1. find the smallest count character c in the array, split the string s with the character c 
   and resursively calling the all the substring, return the max value from them
2. or just find the first character that has count less than k and then do the split

Code: T: O(n), because there are at most 26 levels of recursions.
'''

# TC: O(n)
# SC: O(1)

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # base case
        if len(s) < k: 
            return 0
        
        # get the char with lowest count in s
        c = min(set(s), key = s.count) 
        if s.count(c) >= k: 
            return len(s)

        return max(self.longestSubstring(t, k) for t in s.split(c))
