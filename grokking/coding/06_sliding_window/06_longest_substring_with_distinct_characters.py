#
'''
Given a string, find the length of the longest substring, which has all distinct characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring with distinct characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings with distinct characters are "abc" & "cde".
'''

###############################################################################################################
# sliding window
# TC: O(N)
# SC: O(1)

def non_repeat_strings(word):
  start = 0
  maxlength = 0
  freqmap = {}
  
  for end in range(len(word)):
    right_char = word[end]
    if right_char in freqmap:
      start = max(start, freqmap[right_char] + 1)
    freqmap[right_char] = end
    
    maxlength = max(maxlength, end - start + 1)
  return maxlength
