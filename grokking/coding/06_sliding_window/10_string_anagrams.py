# https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''
Given a string and a pattern, find all anagrams of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N!
N!
 permutations (or anagrams) of a string having N
N
 characters. For example, here are the six anagrams of the string “abc”:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
'''

##########################################################################################################################
# sliding window
# TC: O(N + M)
# SC: O(M)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # store pattern p to hashmap
        freqmap = {}
        for c in p:
            freqmap[c] = freqmap.get(c, 0) + 1
        
        # check in string s
        start = 0
        charmatch = 0
        output = []
        for end in range(len(s)):
            right_char = s[end]
            if right_char in freqmap:
                freqmap[right_char] -= 1
                if freqmap[right_char] == 0: charmatch += 1
                
            # found permutation
            if charmatch == len(freqmap):
                output.append(start)
            
            # slide window
            if end >= len(p) - 1:
                left_char = s[start]
                if left_char in freqmap:
                    if freqmap[left_char] == 0: charmatch -= 1
                    freqmap[left_char] += 1
                start += 1
        return output
        

