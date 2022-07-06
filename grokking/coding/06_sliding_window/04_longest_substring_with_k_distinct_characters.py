#
'''
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
Example 4:

Input: String="cbbebi", K=10
Output: 6
Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".
'''

##############################################################################################################
# sliding window on frequency hashmap
# TC: O(N)
# SC: O(k)

def longest_substring(word, k):
  maxlength = 0
  start = 0
  freqmap = {}
  
  for end in range(len(word)):
    c = word[end]
    freqmap[c] = freqmap.get(c, 0) + 1
    
    # slide window
    if len(freqmap) > k:
      left_c = word[start]
  
      freqmap[left_c] -= 1
      if freqmap[left_c] == 0: del freqmap[left_c]
      start += 1
      
    maxlength = max(maxlength, end - start + 1)
  return maxlength
      
   
      
