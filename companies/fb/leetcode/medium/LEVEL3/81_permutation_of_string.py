'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''

# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# https://leetcode.com/problems/permutation-in-string/discuss/1761953/Python3-SLIDING-WINDOW-OPTIMIZED-(-)-Explained
'''
The only thing we care about any particular substring in s2 is having the same number of characters as in the s1. So we create a hashmap with the count of every character in the string s1. Then we slide a window over the string s2 and decrease the counter for characters that occurred in the window. As soon as all counters in the hashmap get to zero that means we encountered the permutation.

Time: O(n) - linear for window sliding and counter
Space: O(1) - conctant for dictionary with the maximum 26 pairs (English alphabet)
'''

def checkInclusion(self, s1: str, s2: str) -> bool:
	cntr, w = Counter(s1), len(s1)   

	for i in range(len(s2)):
		if s2[i] in cntr: 
			cntr[s2[i]] -= 1
		if i >= w and s2[i-w] in cntr: 
			cntr[s2[i-w]] += 1

		if all([cntr[i] == 0 for i in cntr]): # see optimized code below
			return True

	return False
