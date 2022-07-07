#
'''
Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter, 
find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have the longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have the longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
'''

##################################################################################################################
# sliding window
# TC: O(n)
# SC: O(1)

def length_of_longest_substring(word, k):
  start = 0
  maxlength = 0
  freqmap = 0
  max_freq = 0
  
  for end in range(len(word)):
    right_char = word[end]
    freqmap[right_char] = freqmap.get(right_char, 0) + 1
    max_freq = max(max_freq, freqmap[right_char])
    
    # sliding window shrinks
    window_size = end - start + 1
    if window_size - max_repeat > k:
      left_char = word[start]
      freqmap[left_char] -= 1
      if freqmap[left_char] == 0: del freqmap[left_char]
      start += 1
      
    maxlength = max(maxlength, end - start + 1)
  return maxlength
    
