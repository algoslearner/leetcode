'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

##########################################################################
# Sliding window
# TC: O(m+n)
# SC: O(1)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = t
        search_string = s
        
        target_letter_counts = collections.Counter(target)
        start = 0
        end = 0
        min_window = ""
        target_len = len(target)        
        
        for end in range(len(search_string)):
            if target_letter_counts[search_string[end]] > 0:
                target_len -= 1
            target_letter_counts[search_string[end]] -= 1
            
			# If all letters in the target are found:
            while target_len == 0:
                window_len = end - start + 1
                if not min_window or window_len < len(min_window):
					# Note the new minimum window
                    min_window = search_string[start : end + 1]
                    
				# Increase the letter count of the current letter
                target_letter_counts[search_string[start]] += 1
                
				# If all target letters have been seen and now, a target letter is seen with count > 0
				# Increase the target length to be found. This will break out of the loop
                if target_letter_counts[search_string[start]] > 0:
                    target_len += 1
                    
                start+=1
                
        return min_window
        
        
