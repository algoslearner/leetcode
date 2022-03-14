'''
Given a string s, return the length of the longest repeating substrings. If no repeating substring exists, return 0.

 

Example 1:

Input: s = "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: s = "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: s = "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters.
'''

# TC: O(n^2) 
# SC: O(n) (Set)

class Solution:
    def search(self, S: str, length: int) -> bool:
        visited = set()
        for i in range(len(S)-length+1):
            substring = S[i:i+length]
            if substring in visited: return True
            visited.add(substring)    
        return False
        
    def longestRepeatingSubstring(self, S: str) -> str:
        left, right = 0, len(S)-1
        while left <= right:
            middle = left + (right-left+1)//2
            if self.search(S, middle): left = middle+1
            else: right = middle-1
        return left-1
        
